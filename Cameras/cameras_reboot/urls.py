from django.conf.urls import url, include
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^reboot/(?P<id>[^/]+)/$', curl),
    url(r'^reboot/', reboot)
]
