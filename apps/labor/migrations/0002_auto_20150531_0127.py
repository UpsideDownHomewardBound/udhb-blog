# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '__first__'),
        ('labor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneNumberToInform',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text_level', models.IntegerField()),
                ('call_level', models.IntegerField()),
                ('phone_number', models.ForeignKey(to='people.PhoneNumber')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='laborannouncement',
            options={'get_latest_by': 'reported_at'},
        ),
        migrations.AddField(
            model_name='laborannouncement',
            name='seriousness',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
