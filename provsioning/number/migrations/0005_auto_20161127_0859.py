# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-27 08:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('number', '0004_auto_20161127_0826'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='logpass',
            options={'verbose_name': 'Logpass'},
        ),
        migrations.AlterModelOptions(
            name='mac',
            options={'verbose_name': 'Mac'},
        ),
    ]
