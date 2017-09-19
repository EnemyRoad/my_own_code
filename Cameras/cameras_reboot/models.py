# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Cameras(models.Model):
    class Meta:
        verbose_name = 'камера'
        verbose_name_plural = 'камеры'

    VENDOR_CHOISES = (
        ('Vivotek', 'Vivotek'),
        ('Hikvision', 'Hikvision'),
    )
    ip = models.GenericIPAddressField(verbose_name='IP-address')
    name = models.CharField(max_length=20, verbose_name='Имя камеры')
    vendor = models.CharField(max_length=9, choices=VENDOR_CHOISES, default='Vivotek')

    def __str__(self):
        return self.name
