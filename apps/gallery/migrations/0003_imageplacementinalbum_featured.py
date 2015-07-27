# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20150713_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageplacementinalbum',
            name='featured',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
