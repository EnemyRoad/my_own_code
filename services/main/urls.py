from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^add/$', add_data),
    url(r'^(?P<subject>[^/]+)/save/$', save),
    url(r'^(?P<subject>[^/]+)/$', info),
    url(r'^', home)
]
