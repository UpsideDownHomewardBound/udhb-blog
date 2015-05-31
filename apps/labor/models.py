from hendrix.experience import crosstown_traffic
from the_comm_app.sms import BlastToText
from django.db import models
from datetime import datetime
from django.db.models.signals import post_save


class LaborAnnouncement(models.Model):
    reported_at = models.DateTimeField(default=datetime.now)
    text = models.TextField()
    seriousness = models.IntegerField(default=0)

    class Meta:
        get_latest_by = "reported_at"

    def alert(self):

        @crosstown_traffic.follow_response()
        def send_comm_messages():
            call_recipients = PhoneNumberToInform.objects.filter(call_level__lte=self.seriousness)

            text_recipients = PhoneNumberToInform.objects.filter(text_level__lte=self.seriousness)
            text_blaster = BlastToText(text_recipients)
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
    phone_number = models.ForeignKey('people.PhoneNumber')
    text_level = models.IntegerField()
    call_level = models.IntegerField()