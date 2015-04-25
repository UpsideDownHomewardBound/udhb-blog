from django.db import models
from mezzanine.pages.models import Page


class Place(Page):
    '''
    Places in which we have existed.
    '''

    within = models.ForeignKey("places.Place", related_name="contains", blank=True, null=True)

    def contains_places(self):
        return self.contains.exists()


class Visit(models.Model):
    '''
    Visits are the duration in which we are in a place.
    '''

    place = models.ForeignKey("places.Place", related_name="visits")
    arrival = models.DateTimeField(blank=True, null=True)
    departure = models.DateTimeField(blank=True, null=True)
    visitors = 