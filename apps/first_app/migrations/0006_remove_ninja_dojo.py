# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-18 14:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0005_auto_20180418_0744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ninja',
            name='dojo',
        ),
    ]
