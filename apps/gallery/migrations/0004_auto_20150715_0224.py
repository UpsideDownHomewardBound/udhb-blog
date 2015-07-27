# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_imageplacementinalbum_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageplacementinalbum',
            name='featured',
            field=models.CharField(blank=True, max_length=10, null=True, choices=[(b'R', b'Right'), (b'L', b'Left'), (b'N', b'No Float')]),
            preserve_default=True,
        ),
    ]
