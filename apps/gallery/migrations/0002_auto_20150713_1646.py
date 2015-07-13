# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_squashed_0005_auto_20150707_0337'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='most_recent_image_taken',
            field=models.ForeignKey(related_name='albums_in_which_this_is_the_most_recent_taken', blank=True, to='gallery.Image', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='album',
            name='most_recent_image_uploaded',
            field=models.ForeignKey(related_name='albums_in_which_this_is_the_most_recent_uploaded', blank=True, to='gallery.Image', null=True),
            preserve_default=True,
        ),
    ]
