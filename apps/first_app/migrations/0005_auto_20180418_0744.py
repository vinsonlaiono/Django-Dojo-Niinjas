# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-18 14:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_auto_20180418_0742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ninja',
            name='dojo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ninjas', to='first_app.Dojo'),
        ),
    ]