from django.test import TestCase
from apps.gallery.inventory import gather_albums_and_images
from apps.gallery.models import Album, ImagePlacementInAlbum


class InventoryTests(TestCase):

    def test_proper_gathering(self):
        self.assertFalse(Album.objects.exists())
        gather_albums_and_images('sample-gallery-dump')
        self.assertEqual(Album.objects.count(), 1)
        self.assertEqual(ImagePlacementInAlbum.objects.count(), 4)

    def test_gather_again_does_not_create_new_objects(self):
        self.test_proper_gathering()
        self.assertEqual(Album.objects.count(), 1)
        gather_albums_and_images('sample-gallery-dump')
        self.assertEqual(Album.objects.count(), 1)
        self.assertEqual(ImagePlacementInAlbum.objects.count(), 4)
