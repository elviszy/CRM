# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-04-25 16:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SunFaLongCRM', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='records',
            name='content',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
