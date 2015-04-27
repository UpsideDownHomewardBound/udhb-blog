import datetime
from django.test import TestCase
from apps.places.models import Place


class NewVisitTests(TestCase):

    def test_newvisit_newvisitor(self):


        # database is completely empty

        scotland = Place.objects.create(name="Scotland")

        joe = User
        jane = User

        self.assertFalse(joe.has_been_to, scotland)

        Visit.objects.completely_new(
            visitor = [joe, jane]
            arrival = datetime.datetime.now()
            place = some_place
        )

        self.assertTrue(joe.has_been_to, scotland)

