# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-28 02:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sis', '0002_auto_20180828_0227'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='Frequente',
            field=models.BooleanField(default=False),
        ),
    ]
