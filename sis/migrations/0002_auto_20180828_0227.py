# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-28 02:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sis', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pessoa',
            old_name='Descricao',
            new_name='Telefone',
        ),
    ]
