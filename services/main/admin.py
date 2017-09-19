from django.contrib import admin
from .models import *


# Register your models here.
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['name', 'price_below_100', 'price_up_100']


admin.site.register(Services, ServicesAdmin)
admin.site.register(Data)
admin.site.register(Payment)