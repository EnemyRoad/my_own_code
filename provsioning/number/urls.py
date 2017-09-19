from django.conf.urls import url
from .views import config

urlpatterns = (
    url(r'^(?P<macadr>\w+).cfg$', config),
)
