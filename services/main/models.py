# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Services(models.Model):
    class Meta:
        verbose_name = 'услуга'
        verbose_name_plural = 'услуги'

    name = models.CharField(max_length=20, verbose_name='Услуга')
    id_name = models.CharField(max_length=20, verbose_name='Имя для ссылки(транслит)', unique=True)
    price_below_100 = models.FloatField(verbose_name='Стоимость до 100')
    price_up_100 = models.FloatField(verbose_name='Стоимость после 100')

    def __unicode__(self):
        return self.name


class Data(models.Model):
    class Meta:
        verbose_name = 'показания'
        verbose_name_plural = 'показания'

    service = models.ForeignKey(Services, verbose_name='Услуга')
    meters_data = models.IntegerField(verbose_name='Данные со счетчика')
    month = models.DateField(verbose_name='Месяц')

    def __unicode__(self):
        return self.service.name + ' за ' + self.month.strftime('%B-%Y')


class Payment(models.Model):
    class Meta:
        verbose_name = 'к оплате'
        verbose_name_plural = 'к оплате'
    name = models.ForeignKey(Data)
    delay = models.IntegerField(verbose_name='Накручено')
    count = models.FloatField(verbose_name='К оплате')

    def __unicode__(self):
        return self.name.service.name + ' за ' + self.name.month.strftime('%B-%Y')