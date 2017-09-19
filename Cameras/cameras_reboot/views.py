from django.shortcuts import render, render_to_response, redirect
from .models import *
from django.conf import settings


# Create your views here.
# Reboot camera
def reboot(request):
    args = {'Cameras': Cameras.objects.all()}
    return render_to_response('home.html', args)


def curl(request, id):
    import pycurl
    item = Cameras.objects.get(id=id)
    obj = pycurl.Curl()
    if item.vendor == 'Vivotek':
        obj.setopt(pycurl.URL,
                   "http://" + settings.VIVOTEK_USER + ":" + settings.VIVOTEK_PASS + "@" + item.ip + "/cgi-bin/admin/setparam.cgi?system_reset=0")
    else:
        obj.setopt(pycurl.URL,
                   "http://" + settings.HIKVISION_USER + ":" + settings.HIKVISION_PASS + "@" + item.ip + "/System/reboot")
        obj.setopt(pycurl.CUSTOMREQUEST, "PUT")
    obj.perform()
    return redirect('/reboot/')
