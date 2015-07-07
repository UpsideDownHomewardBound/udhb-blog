# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20150704_1949'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='date',
            new_name='taken',
        ),
        migrations.AddField(
            model_name='image',
            name='uploaded',
            field=models.DateTimeField(default=datetime.datetime.now),
            preserve_default=True,
        ),
    ]
