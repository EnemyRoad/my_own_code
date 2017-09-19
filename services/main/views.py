# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect, HttpResponse
from .models import *
from .forms import *
from datetime import date, datetime
from django.template.context_processors import csrf


# Create your views here.


def home(request):
    args = {}
    args['curr'] = Payment.objects.filter(name__month__month=date.strftime(datetime.now(), '%m'),
                                       name__month__year=date.strftime(datetime.now(), '%Y'))
    curr_month = date.strftime(datetime.now(), '%m')
    prew_month = '0' + str(int(curr_month, 0) - 1)
    args['prew'] = Payment.objects.filter(name__month__month=prew_month,
                                       name__month__year=date.strftime(datetime.now(), '%Y'))
    return render_to_response('home.html', args)


def info(request, subject):
    args = {}
    a = Payment.objects.filter(name__service__id_name=subject)
    for item in a:
        print (item.count)
    args['data'] = Data.objects.filter(service__id_name=subject)

    args['service'] = Services.objects.get(id_name=subject)
    args['payment'] = Payment.objects.filter(name__service__id_name=subject)
    return render_to_response('info.html', args)


def calculator(subject):
    curr_month = date.strftime(datetime.now(), '%m')
    prew_month = '0' + str(int(curr_month, 0) - 1)
    data_now = Data.objects.get(service__id_name=subject, month__month=curr_month,
                                month__year=date.strftime(datetime.now(), '%Y'))
    data_prew = Data.objects.get(service__id_name=subject, month__month=prew_month,
                                 month__year=date.strftime(datetime.now(), '%Y'))
    delay = data_now.meters_data - data_prew.meters_data
    if delay <= 100:
        summ = delay * Services.objects.get(id_name=subject).price_below_100
    else:
        delay_new = delay - 100
        summ = (100 * Services.objects.get(id_name=subject).price_below_100) + (
            delay_new * Services.objects.get(id_name=subject).price_up_100)
    return summ, delay, data_now.meters_data, data_prew.meters_data


def add_data(request):
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        form = AddData(request.POST)
        if form.is_valid():
            form.save()
            args['form'] = form
        return redirect('/')
    form = AddData()
    args['form'] = form
    return render_to_response('add.html', args)


def save(request, subject):
    summ = calculator(subject).__getitem__(0)
    delay = calculator(subject).__getitem__(1)
    Payment.objects.create(
        name=Data.objects.get(service__id_name=subject, month__month=date.strftime(datetime.now(), '%m'),
                              month__year=date.strftime(datetime.now(), '%Y')), count=summ, delay=delay)
    return redirect('/' + subject + '/')
