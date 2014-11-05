# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0003_auto_20141104_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='font_size',
            field=models.IntegerField(default=700),
            preserve_default=False,
        ),
    ]
