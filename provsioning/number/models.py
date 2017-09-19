from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Logpass(models.Model):
    class Meta:
        db_table = 'Logpass'
        verbose_name = "Logpass"

    number = models.CharField(max_length=10)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.number


class Mac(models.Model):
    class Meta:
        db_table = 'mac'
        verbose_name = 'Mac'

    mac = models.CharField(max_length=20)
    number = models.ForeignKey(Logpass, on_delete=models.CASCADE)

    def __str__(self):
        return self.mac
