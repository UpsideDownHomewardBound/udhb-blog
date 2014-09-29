from django.db import models
from mezzanine.core.fields import FileField
from django.utils.translation import ugettext_lazy as _


class BannerImage(models.Model):
    image = FileField(verbose_name=_("Banner Image"),
        format="Image", max_length=255, null=True, blank=True)
