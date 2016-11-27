# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=512)),
                ('email', models.EmailField(max_length=254)),
                ('descr', models.TextField()),
                ('post_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(max_length=128)),
            ],
        ),
    ]
