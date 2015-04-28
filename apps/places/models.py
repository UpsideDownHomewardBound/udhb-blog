from django.db import models
from django.conf import settings
from mezzanine.pages.models import Page


class Place(models.Model):
    '''
    Places in which we have existed.
    '''

    name = models.CharField(max_length=50)
    within = models.ForeignKey("places.Place", related_name="contains", blank=True, null=True)

    def contains_places(self):
        return self.contains.exists()

    def users_who_have_visited(self):
        return  # TODO


class VisitManager(models.Manager):

    def completely_new(self, stuff):
        pass


class Visit(models.Model):
    '''
    Visits are the duration in which we are in a place.
    '''

    object = VisitManager()

    place = models.ForeignKey("places.Place", related_name="visits")

    def end(self):
        '''
        The latest datetime of departure for a Visitor.

        If any Visitors have not yet departed, returns None.
        '''
        pass


class Arrival(models.Model):
    visit = models.ForeignKey("places.Visit")
    datetime = models.DateTimeField()


class Departure(models.Model):
    concludes = models.ForeignKey(Arrival)
    datetime = models.DateTimeField()


class Visitor(models.Model):
    '''
    A person engaging in a visit.

    If the same person leaves a visit and returns to it, we will
    make a new Visitor instance.
    '''
    person = models.ForeignKey(settings.AUTH_USER_MODEL)
    arrival = models.ForeignKey(Arrival)
    departure = models.ForeignKey(Departure)

    def is_first_appearance(self):
        pass


class TravelMode(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()


class Journey(models.Model):
    beginning = models.ForeignKey(Visit, related_name="launchings")
    ending = models.ForeignKey(Visit, related_name="landings")
    mode = models.ForeignKey(TravelMode)
    description = models.TextField()