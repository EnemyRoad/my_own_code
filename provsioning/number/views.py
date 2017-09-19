from django.shortcuts import render
from number.models import Mac


# Create your views here.
def config(request, macadr):
    context = {
        'Config': Mac.objects.filter(mac=macadr),
    }
    return render(request, 'number/0000000000.cfg', context)