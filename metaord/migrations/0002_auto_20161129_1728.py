# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models, migrations
from metaord.utils.auth import Groups


def add_group_permissions(apps, schema_editor): 
    # app = apps.get_app_config('metaord')
    # app.models_module = app.models_module or True
    # update_contenttypes(app) # make sure all content types exist
    Groups.get_or_create_operator()
    Groups.get_or_create_boss()

class Migration(migrations.Migration):

    dependencies = [
        ('metaord', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_group_permissions)
    ]
