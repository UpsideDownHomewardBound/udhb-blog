# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_auto_20150715_0224'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='album_initialized',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 19, 22, 20, 28, 930084, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
