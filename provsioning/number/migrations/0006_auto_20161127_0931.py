# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-27 09:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('number', '0005_auto_20161127_0859'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logpass',
            old_name='tel_num',
            new_name='number',
        ),
        migrations.RenameField(
            model_name='logpass',
            old_name='tel_pass',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='mac',
            old_name='mac_adr',
            new_name='mac',
        ),
        migrations.RenameField(
            model_name='mac',
            old_name='mac_number',
            new_name='number',
        ),
    ]
