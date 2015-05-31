from django.test import TestCase
from apps.labor.models import LaborAnnouncement

from hendrix.utils.test_utils import AsyncTestMixin
from hendrix.experience import crosstown_traffic


class LaborAnnouncementTests(TestCase, AsyncTestMixin):

    def test_new_announcement_cases_alert(self):
        la = LaborAnnouncement.objects.create(text="Test-1-2-3",
                                         seriousness=0)
        c = crosstown_traffic

        self.assertNumCrosstownTasks(1)

        next_task = self.next_task()
        next_task()

        self.fail()

    def test_save_old_announcement_causes_no_new_alert(self):
        self.fail()