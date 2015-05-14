from django.db import models
from datetime import datetime


class LaborAnnouncement(models.Model):
    reported_at = models.DateTimeField(default=datetime.now)
    text = models.TextField()

    def __unicode__(self):
        return self.text


class ContractionEvent(LaborAnnouncement):
    ended = models.DateTimeField(blank=True, null=True)
    began = models.DateTimeField()
    duration = models.IntegerField(help_text="The number of seconds a contraction lasts.")
    interval = models.IntegerField(help_text="The number of seconds between contractions.")

    def __unicode__(self):
        "%s: contractions were %s long, starting at %s" % (self.text,
                                                           self.duration,
                                                           self.began)

    def previous(self):
        '''
        returns the ContractionEvent object that occurred before this one.
        '''
        #  ContractionEvent.objects.order_by('ended')


# post_save.announce(LaborAnnouncement, blast_to_text)


def blast_to_text(labor_announcement):
    from theCommApp.sms import BlastToText
    text_blaster = BlastToText()

    recipients = PhoneNumber.objects.filter(owner__labor_updates_via_text=True)