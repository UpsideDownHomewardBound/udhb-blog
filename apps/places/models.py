from django.db import models
from django.conf import settings
from mezzanine.pages.models import Page


class Place(Page):
    '''
    Places in which we have existed.
    '''

    name = models.CharField()
    within = models.ForeignKey("places.Place", related_name="contains", blank=True, null=True)

    def contains_places(self):
        return self.contains.exists()


class VisitManager(models.Manager):

    def completely_new(self, stuff):
        pass



class Visit(models.Model):
    '''
    Visits are the duration in which we are in a place.
    '''

    object = VisitManager()

    place = models.ForeignKey("places.Place", related_name="visits")


class VisitBookEnd(models.Model):

    class Meta:
        abstract = True

    visit = models.ForeignKey("places.Visit")
    datetime = models.DateTimeField()


class Arrival(VisitBookEnd):
    pass


class Departure(VisitBookEnd):
    pass


class Visitor(models.Model):
    person = models.ForeignKey(settings.AUTH_USER_MODEL)
    arrival = models.ForeignKey(Arrival)
    departure = models.ForeignKey(Departure)


class TravelMode(models.Model):
    name = models.CharField()
    description = models.TextField()


class Journey(models.Model):
    beginning = models.ForeignKey(Visit)
    ending = models.ForeignKey(Visit)
    mode = models.ForeignKey(TravelMode)
    description = models.TextField()