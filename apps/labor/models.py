from hendrix.experience import crosstown_traffic
from the_comm_app.sms import BlastToText
from django.db import models
from datetime import datetime
from django.db.models.signals import post_save
from settings.secrets import TWILIO_SID, TWILIO_AUTH


class LaborAnnouncement(models.Model):
    reported_at = models.DateTimeField(default=datetime.now)
    text = models.TextField()
    seriousness = models.IntegerField(default=0)

    class Meta:
        get_latest_by = "reported_at"

    def alert(self):

        @crosstown_traffic.follow_response()
        def send_comm_messages():
            call_recipients = PhoneNumberToInform.objects.filter(call_level=0)
            text_recipients = PhoneNumberToInform.objects.filter(text_level=0).values_list('phone_number__number', flat=True)

            text_blaster = BlastToText(TWILIO_SID,
                                       TWILIO_AUTH,
                                       from_number="+16468462229",
                                       recipients=text_recipients)

            try:
                ce = self.contractionevent
                message = "%s. Contractions %s minutes apart, each lasting %s seconds." % (self.text, ce.interval/60, ce.duration)
            except LaborAnnouncement.DoesNotExist:
                message = self.text

            text_blaster.message = message

            text_blaster.send()

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.alert()

        return super(LaborAnnouncement, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.text


class ContractionEvent(LaborAnnouncement):
    ended = models.DateTimeField(blank=True, null=True)
    began = models.DateTimeField()
    duration = models.IntegerField(help_text="The number of seconds a contraction lasts.")
    interval = models.IntegerField(help_text="The number of seconds between contractions.")

    def __unicode__(self):
        return "ContractionEvent reported at %s" % self.reported_at

    def previous(self):
        '''
        returns the ContractionEvent object that occurred before this one.
        '''
        #  ContractionEvent.objects.order_by('ended')


class PhoneNumberToInform(models.Model):
    phone_number = models.ForeignKey('people.PhoneNumber', unique=True)
    text_level = models.IntegerField()
    call_level = models.IntegerField()

    def __unicode__(self):
        return str(self.phone_number)