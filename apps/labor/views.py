import functools
from django.contrib.humanize.templatetags.humanize import naturaltime
from hendrix.experience import crosstown_traffic
from the_comm_app.plumbing import PhoneLine
from the_comm_app.voice.features import CallBlast
from twilio.rest.exceptions import TwilioRestException
from apps.labor.models import LaborAnnouncement, ContractionEvent
from the_comm_app.voice.dispositions import ConferenceHoldingPattern, Voicemail
from settings.secrets import TWILIO_SID, TWILIO_AUTH


def all_announcements(request):
    announcements = LaborAnnouncement.objects.all()

    return render('labor_announcements.html',
        {'announcements': announcements}
    )


class BirthCallBlast(CallBlast):

    phones = '+18106233203',
    clients = '1_justin_mobile',
    inquiry_addendum = "This is the birth information line. Press any key to answer this call."

    def last_stop_before_vegas(self):
        conference = self.line.client.conferences.list(
            friendly_name=self.conference_id,
            status="in-progress"
        )
        if conference:
            self.no_go = True


class OurHoldingPattern(ConferenceHoldingPattern):

    hold_music = "http://kayemyles.com/static/chocobo.wav"


class BirthLine(PhoneLine):

    name = "birth_line"
    number_to_use_for_outgoing_calls = "+16468462229"
    domain = "kayemyles.com"

    twilio_sid = TWILIO_SID
    twilio_auth = TWILIO_AUTH

    greeting_text = "Thanks for calling Chelsea and Justin's birth information line."
    disposition = [OurHoldingPattern]
    features = [BirthCallBlast]
    nobody_home = Voicemail

    runner = crosstown_traffic.follow_response()
    conference_name = "Nethram"

    voice = "alice"
    language = "en-AU"

    def customize_disposition(self, gather):

        say = functools.partial(gather.addSay, voice=self.voice, language=self.language)
        say("Press any key to join the conference.", language="en", voice="man")
        say("Here are the latest details.")

        # LaborAnnouncements

        announcements = LaborAnnouncement.objects.order_by('-reported_at')

        qualifiers = ['%s the following was reported:',
                      'Before that, %s, this report:',
                      'Going back further to %s, we have:',
                      ]

        for counter, a in enumerate(announcements):
            try:
                q = qualifiers[counter]
            except IndexError:
                q = qualifiers[2]

            say(q % naturaltime(a.reported_at).replace(u'\xa0', u' '))

            try:
                ce = a.contractionevent
                began = naturaltime(ce.began).replace(u'\xa0', u' ')
                say("Chelsea reported contractions %s minutes apart, each lasting %s seconds.  These began %s." % (ce.interval/60, ce.duration, began))
                if ce.text:
                    say("At this time, the following was also reported.")
                    say(ce.text)

            except LaborAnnouncement.DoesNotExist:
                say(a.text)


               # Every other announcement, remind them of the conference.
            if (counter % 2) == 0:
                say("At any time, you may press any key to be connected to the conference.", language="en", voice="man")

        say("No further information is available.  Join the conference to talk to the birth team.")