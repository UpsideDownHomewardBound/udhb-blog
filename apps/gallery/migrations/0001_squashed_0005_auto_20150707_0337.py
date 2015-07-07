# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    replaces = [('gallery', '0001_initial'), ('gallery', '0002_auto_20150703_1529'), ('gallery', '0003_auto_20150704_1949'), ('gallery', '0004_auto_20150706_1612'), ('gallery', '0005_auto_20150707_0337')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('slug', models.SlugField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('filename', models.CharField(max_length=200)),
                ('date', models.DateTimeField(null=True, blank=True)),
                ('full_url', models.CharField(max_length=200)),
                ('show_url', models.CharField(max_length=200)),
                ('thumb_url', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ImagePlacementInAlbum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('caption', models.CharField(max_length=200)),
                ('order', models.IntegerField()),
                ('album', models.ForeignKey(to='gallery.Album')),
                ('image', models.ForeignKey(to='gallery.Image')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='imageplacementinalbum',
            unique_together=set([('image', 'album', 'order')]),
        ),
        migrations.AlterField(
            model_name='imageplacementinalbum',
            name='album',
            field=models.ForeignKey(related_name='placements', to='gallery.Album'),
            preserve_default=True,
        ),
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
        migrations.RenameField(
            model_name='image',
            old_name='date',
            new_name='taken',
        ),
        migrations.AddField(
            model_name='image',
            name='datetime_uploaded',
            field=models.DateTimeField(default=datetime.datetime.now),
            preserve_default=True,
        ),
        migrations.RenameField(
            model_name='image',
            old_name='taken',
            new_name='datetime_taken',
        ),
    ]
