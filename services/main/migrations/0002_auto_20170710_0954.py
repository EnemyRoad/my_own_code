# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-10 09:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.FloatField(verbose_name='\u041a \u043e\u043f\u043b\u0430\u0442\u0435')),
            ],
        ),
        migrations.AlterModelOptions(
            name='data',
            options={'verbose_name': '\u043f\u043e\u043a\u0430\u0437\u0430\u043d\u0438\u044f', 'verbose_name_plural': '\u043f\u043e\u043a\u0430\u0437\u0430\u043d\u0438\u044f'},
        ),
        migrations.AlterField(
            model_name='data',
            name='meters_data',
            field=models.FloatField(verbose_name='\u0414\u0430\u043d\u043d\u044b\u0435 \u0441\u043e \u0441\u0447\u0435\u0442\u0447\u0438\u043a\u0430'),
        ),
        migrations.AlterField(
            model_name='services',
            name='price_below_100',
            field=models.FloatField(verbose_name='\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0434\u043e 100'),
        ),
        migrations.AlterField(
            model_name='services',
            name='price_up_100',
            field=models.FloatField(verbose_name='\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u043f\u043e\u0441\u043b\u0435 100'),
        ),
        migrations.AddField(
            model_name='payment',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Data'),
        ),
    ]
