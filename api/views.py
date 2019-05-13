from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.


def api_list(request):
    return

def timestamp(request):
    return render(request, 'api/timestamp.html',  {})

def utc_string(request, date_number):
    return HttpResponse(datetime.datetime.utcfromtimestamp(date_number).strftime('%Y-%m-%d %H:%M:%S'))
