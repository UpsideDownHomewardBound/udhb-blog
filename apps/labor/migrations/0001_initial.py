# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LaborAnnouncement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reported_at', models.DateTimeField(default=datetime.datetime.now)),
                ('text', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ContractionEvent',
            fields=[
                ('laborannouncement_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='labor.LaborAnnouncement')),
                ('ended', models.DateTimeField(null=True, blank=True)),
                ('began', models.DateTimeField()),
                ('duration', models.IntegerField(help_text=b'The number of seconds a contraction lasts.')),
                ('interval', models.IntegerField(help_text=b'The number of seconds between contractions.')),
            ],
            options={
            },
            bases=('labor.laborannouncement',),
        ),
    ]
