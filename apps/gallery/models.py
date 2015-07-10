from datetime import datetime
from django.core.exceptions import ValidationError
from django.db import models

import pyrax
import urllib
import urlparse
import logging
logger = logging.getLogger(__name__)


class Image(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    filename = models.CharField(max_length=200)
    datetime_taken = models.DateTimeField(blank=True, null=True)
    datetime_uploaded = models.DateTimeField(default=datetime.now)

    full_url = models.CharField(max_length=200)
    show_url = models.CharField(max_length=200)
    thumb_url = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        if not (self.full_url and self.show_url and self.thumb_url):
            raise ValidationError('All urls must be provided for an Image object.')
        else:
            super(Image, self).save(*args, **kwargs)

    def rack(self, size, file_path, container, format):
        logger.info("Racking %s, %s size, to %s" % (file_path, size, container))
        with open(file_path) as f:
            full_name = "%s-%s" % (self.filename, size)
            logger.info("Uploading %s" % full_name)
            cdn_obj = container.store_object(
                full_name,
                f,
                content_type="image/%s" % format,
            )
            logger.info("Done uploading %s" % full_name)
            encoded_name = urllib.quote(cdn_obj.name)
            setattr(self,
                    "%s_url" % size,
                    urlparse.urljoin(container.cdn_uri, encoded_name)
                    )
            logger.info("Finished racking %s at %s size." % (full_name, size))


class Album(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField()

    def __unicode__(self):
        return self.name

    @property
    def container(self):
        # This is effectively a get-or-create flow.
        try:
            return self.container_obj
        except AttributeError:
            return pyrax.cloudfiles.create_container(self.slug)

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.slug.replace('-', ' ').capitalize()

        if not self.id:  # We only need to create the container the first time.
            self.container_obj = pyrax.cloudfiles.create_container(self.slug)
            self.container_obj.make_public()
        return super(Album, self).save(*args, **kwargs)


class ImagePlacementInAlbum(models.Model):
    image = models.ForeignKey(Image)
    album = models.ForeignKey(Album, related_name='placements')
    caption = models.CharField(max_length=200, blank=True, null=True)
    order = models.IntegerField()

    class Meta:
        unique_together = ('image', 'album', 'order')
        ordering = ['order']