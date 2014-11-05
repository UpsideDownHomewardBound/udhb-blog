from django.db import models
from mezzanine.core.fields import FileField
from django.utils.translation import ugettext_lazy as _


class Theme(models.Model):
    name = models.CharField(max_length=50)
    banner_image = FileField(verbose_name=_("Banner Image"),
        format="Image", max_length=255)
    heading_style = models.CharField(max_length=250, null=True, blank=True)
    font_size = models.IntegerField()

    def __unicode__(self):
      return self.name
