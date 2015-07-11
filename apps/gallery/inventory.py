import os
from datetime import datetime
from PIL import Image as PILImage
import exifread
from apps.gallery.models import Album, Image, ImagePlacementInAlbum
import logging
from django.conf import settings

logger = logging.getLogger("inventory")


GALLERY_ROOT = '%s/gallery-holder' % settings.PROJECT_ROOT
THUMBNAIL_WIDTH = 125


def gather_albums_and_images(gallery_dir):
    '''
    Walk through gallery_dir, record each subdirectory as an Album,
    with each file in it as an Image in that Album.
    '''
    import pyrax
    from settings.secrets import RACKSPACE_API_KEY
    logger.info("Connecting to Rackspace.")
    pyrax.set_setting("identity_type", "rackspace")
    pyrax.set_default_region('IAD')
    pyrax.set_credentials('ckaye89', RACKSPACE_API_KEY)
    logger.info("Finished connecting to Rackspace.")

    for counter, (subdir, dirs, image_files) in enumerate(os.walk(gallery_dir)):

        # Ignore root directory; we only want subdirectories.
        if subdir == gallery_dir:
            continue

        # Get or create the album corresponding to this dir.
        album_slug = subdir.split('/')[-1]
        album, album_created = Album.objects.get_or_create(slug=album_slug)
        container = album.container
        os.mkdir("%s/%s" % (subdir, "temp_image_resizing"))

        # Make picture objects for each file
        for filename in image_files:
            full_path = "%s/%s" % (subdir, filename)

            try:
                Image.objects.get(filename=filename)
                logger.info("We already have a file called %s" % filename)

                # We can do any update logic here.
                continue

            except Image.DoesNotExist:
                logger.info("%s is a new file.  Creating Image object." % filename)

                with open(full_path) as f:
                    exif_tags = exifread.process_file(
                        f,
                        details=False,
                        stop_tag='EXIF DateTimeOriginal')

                    picture_taken_tag = exif_tags.get('EXIF DateTimeOriginal', None)

                    if picture_taken_tag:
                        picture_taken_unicode = picture_taken_tag.values
                        picture_taken_datetime = datetime.strptime(picture_taken_unicode + 'UTC', '%Y:%m:%d %H:%M:%S%Z')
                        logger.info("Picture taken at %s" % picture_taken_unicode)

                    else:
                        # We didn't glean an EXIF tag for the datetime, so None.
                        logger.info("Image has no 'taken at' datetime.")
                        picture_taken_datetime = None

                image = Image(
                    filename=filename,
                    datetime_taken=picture_taken_datetime,
                )

                # Create gallery size and thumb-size files.
                logger.info("Opening %s to resize." % full_path)
                im = PILImage.open(full_path)

                # Figure out if the picture needs to be rotated and rotate it.
                try:
                    orientation_value = exif_tags['Image Orientation'].values[0]
                except KeyError:
                    orientation_value = None
                rotate_values = {
                    3: 180,
                    6: 270,
                    8: 90
                }
                if orientation_value in rotate_values:
                    # Rotate and save the picture
                    rotation = rotate_values[orientation_value]
                    logger.info("Rotating %s %s degrees" % (full_path, rotation))
                    im = im.rotate(rotation)
                    im.save(full_path)

                show_filename = os.path.splitext(filename)[0] + "-show"
                show_full_path = "%s/temp_image_resizing/%s" % (subdir, show_filename)
                show = im.copy()
                height = im.size[1] / ((im.size[0] / 1600) or 1)
                show.thumbnail((1600, height), PILImage.ANTIALIAS)
                logger.info("Saving show size at %s" % show_full_path)
                show.save(show_full_path, "JPEG")

                thumb_filename = os.path.splitext(filename)[0] + "-thumb"
                thumb_full_path = "%s/temp_image_resizing/%s" % (subdir, thumb_filename)
                thumb = im.copy()
                height = im.size[1] / ((im.size[0] / 1600) or 1)
                thumb.thumbnail((150, height), PILImage.ANTIALIAS)
                logger.info("Saving thumb size at %s" % thumb_full_path)
                thumb.save(thumb_full_path, "JPEG")

                image.rack('full', full_path, container, im.format)
                image.rack('show', show_full_path, container, im.format)
                image.rack('thumb', thumb_full_path, container, im.format)

                logger.info("Ready to save Image and ImagePlacement.")
                image.save()
                ImagePlacementInAlbum.objects.create(
                    image=image,
                    album=album,
                )

                logger.info("Finished gathering %s.  Removing temp files." % filename)
                os.remove(show_full_path)
                os.remove(thumb_full_path)

        # If the album is newly created, set the order by taken_datetime.
        if album_created:
            for counter, placement in enumerate(album.placements.order_by('image__datetime_taken')):
                placement.order = counter * 10
                placement.save()

        os.rmdir("%s/%s" % (subdir, "temp_image_resizing"))


if __name__ == "__main__":
    gather_albums_and_images(GALLERY_ROOT)