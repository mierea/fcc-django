from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import datetime
import time
# Create your views here.


def api_list(request):
    return HttpResponse('test')

def timestamp(request):
    return render(request, 'api/timestamp.html',  {})

def utc_string(request, date_number):
    date_string = datetime.datetime.fromtimestamp(
        int(date_number)
    ).strftime('%a,  %d %b %Y %H:%M:%S GMT')

    return JsonResponse({"unix":  date_number, "utc": date_string })

def day_string(request, uyear, umonth, uday):
    s = "%s/%s/%s" %(uday, umonth, uyear)
    date_number = datetime.datetime.strptime(s, "%d/%m/%Y").timestamp()
    return utc_string(request, date_number)

