# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-31 08:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_socialapps'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='display_name',
            field=models.CharField(max_length=100),
        ),
    ]
