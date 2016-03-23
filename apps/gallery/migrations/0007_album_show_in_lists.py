# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_auto_20160217_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='show_in_lists',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
