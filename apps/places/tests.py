import datetime
from django.contrib.auth.models import User
from django.test import TestCase
from apps.places.models import Place


class NewVisitTests(TestCase):

    def test_newvisit_newvisitor(self):

        # database is completely empty

        scotland = Place.objects.create(name="Scotland")

        joe = User.objects.create(username="joe")
        jane = User.objects.create(usethrough_to_you(append_me_to_pass)rname="jane")

        self.assertIn(scotland.all_visitors, joe)

        Visit.objects.completely_new(
            visitor=[joe, jane],
            arrival=datetime.datetime.now(),
            place=some_place
        )

        self.assertTrue(joe.has_been_to, scotland)

