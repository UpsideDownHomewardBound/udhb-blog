from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.pages.fields

class AddFieldToOtherApp(migrations.AddField):

     def __init__(self, app_name, *args, **kwargs):
        self.app_name = app_name
        return super(AddFieldToOtherApp, self).__init__(*args, **kwargs)

     def state_forwards(self, app_label, state):
        return super(AddFieldToOtherApp, self).state_forwards(self.app_name, state)

class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0002_theme'),
        ('pages', '0001_initial'),
    ]

    operations = [
        AddFieldToOtherApp(
            app_name='pages',
            model_name='page',
            name='theme',
            field=models.ForeignKey(blank=True, to='blogging.Theme', null=True),
            preserve_default=True,
        ),
        AddFieldToOtherApp(
            app_name='pages',
            model_name='page',
            name='in_menus',
            field=mezzanine.pages.fields.MenusField(max_length=100,
						    null=True,
						    verbose_name='Show in menus',
						    blank=True),
        ),
    ]
