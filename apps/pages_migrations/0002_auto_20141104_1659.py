# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.pages.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0002_theme'),
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='theme',
            field=models.ForeignKey(blank=True, to='blogging.Theme', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='in_menus',
            field=mezzanine.pages.fields.MenusField(max_length=100, null=True, verbose_name='Show in menus', blank=True),
            preserve_default=True,
        ),
    ]
