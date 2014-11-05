# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0002_theme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theme',
            name='font',
        ),
        migrations.RemoveField(
            model_name='theme',
            name='font_color',
        ),
        migrations.AddField(
            model_name='theme',
            name='heading_style',
            field=models.CharField(max_length=250, null=True, blank=True),
            preserve_default=True,
        ),
    ]
