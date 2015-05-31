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
    domain = "kayemyles.com:8555"

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
        say("Press any key to join the conference.", language="en-GB", voice="man")

        say("Here are the latest details.")

        most_recent_announcement = LaborAnnouncement.objects.latest()
        most_recent_contraction_report = ContractionEvent.objects.latest()

        say("%s, the following was reported:" % naturaltime(most_recent_announcement.reported_at).replace(u'\xa0', u' '))
        say(most_recent_announcement.text)

        began = naturaltime(most_recent_contraction_report.began).replace(u'\xa0', u' ')

        say("Chelsea reported contractions %s minutes apart, each lasting %s seconds.  These began %s." % (most_recent_contraction_report.interval/60, most_recent_contraction_report.duration, began))

        if most_recent_announcement.contractionevent == most_recent_contraction_report:
            next_la = LaborAnnouncement.objects.filter(contractionevent__isnull=True).latest()
            say("Also, %s, the following was reported:" % naturaltime(next_la.reported_at).replace(u'\xa0', u' '))
            say(next_la.text)
        else:
            say("These contractions were reported %s" % naturaltime(most_recent_contraction_report.reported_at).replace(u'\xa0', u' '))
            if most_recent_contraction_report.text:
                say("At this time, the following was also reported.")
                say(most_recent_contraction_report.text)

        say("Press any key to join the conference.", language="en-GB", voice="man")