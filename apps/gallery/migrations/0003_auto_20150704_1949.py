# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20150703_1529'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imageplacementinalbum',
            options={'ordering': ['order']},
        ),
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='imageplacementinalbum',
            name='caption',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
    ]
