# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_auto_20150706_1612'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='taken',
            new_name='datetime_taken',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='uploaded',
            new_name='datetime_uploaded',
        ),
    ]
