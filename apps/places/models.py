from django.db import models
from mezzanine.pages.models import Page


class Place(Page):
    '''
    Places we have existed in.
    '''

    within = models.ForeignKey("places.Place", related_name="contains", blank=True, null=True)

    def contains_places(self):
        return self.contains.exists()
