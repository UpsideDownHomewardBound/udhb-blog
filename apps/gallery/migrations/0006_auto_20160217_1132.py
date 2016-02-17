# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_album_album_initialized'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageplacementinalbum',
            name='caption',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
    ]
