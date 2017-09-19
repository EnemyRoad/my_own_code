from django.contrib import admin
from .models import *


# Register your models here.
class CamerasAdmin(admin.ModelAdmin):
    list_display = ('name', 'ip')


admin.site.register(Cameras, CamerasAdmin)
