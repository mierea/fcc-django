from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.db import IntegrityError

import datetime
from .forms import ShorturlForm, MetadataForm,ExerciseUserForm, ExerciseForm
from .models import Shorturl, User
import os


def api_list(request):
    return HttpResponse('test')

# Timestamp Microservice
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

# Request header parser
def header_parser(request):
    return render(request, 'api/request_header_parser.html', {})

def whoami(request):
    # print (request.headers.keys())
    return JsonResponse({
        "ipaddress": request.META['REMOTE_ADDR'],
        "language": request.headers['Accept-Language'],
        "software": request.headers['User-Agent'],
    })

# URL Shortener Microservice
def shorturl(request):
    return render(request, 'api/shorturl.html', {'form': ShorturlForm() })

def shorturl_redirect(request, pk):
    try:
        url = Shorturl.objects.get(pk=pk)
    except Shorturl.DoesNotExist:
        form = ShorturlForm()
        return render(request, 'api/shorturl.html', {'form': form, 'error': 'URL does not exist'})
    return redirect(url.original_url)

def shorturl_new(request):
    if  request.method == "POST":
        form = ShorturlForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.original_url = request.POST['original_url']
            post.save()
            return JsonResponse({"original_url": post.original_url, "short_url": post.pk})
    form = ShorturlForm()
    return render(request, 'api/shorturl.html', {'form': form})

# File Metadata Microservice
def file_metadata(request):
    if request.method == "POST":
        form = MetadataForm(request.POST, request.FILES)

        if form.is_valid():
            return JsonResponse({
                "name": request.FILES['file'].name.split(".")[0],
                "type": request.FILES['file'].name.split(".")[1].lower(),
                "size": request.FILES['file'].size,
            })

    form = MetadataForm()
    return render(request, 'api/metadata.html', {"form": form})


# Exercise Tracker Microservice
def exercise(request):
    context = {'form_user': ExerciseUserForm(), 'form_exercise': ExerciseForm()}
    return render(request, 'api/exercise.html', context)


def exercise_new_user(request):
    # Path `username` is required.
    # username already taken
    if request.method == "POST":
        form = ExerciseUserForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)

            post.username = request.POST['username']
            post.save()
            return JsonResponse({
                "username": post.username,
                "_id": post.pk
            })
        else:
            return JsonResponse({"error": form.errors})


    context = {'form_user': ExerciseUserForm(), 'form_exercise': ExerciseForm()}
    return render(request, 'api/exercise.html', context)


def exercise_add(request):
    if request.method == "POST":
        form = ExerciseForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)

            post.user = User.objects.get(pk=request.POST['user'])

            post.description = request.POST['description']
            post.duration = request.POST['duration']
            post.date = request.POST['date']

            post.save()
            return JsonResponse({
                "userid": post.user.pk,
                "username": post.user.username,
                "description": post.description,
                "duration": post.duration,
                "date": post.date,

            })
        else:
            return JsonResponse({"error": form.errors})


    context = {'form_user': ExerciseUserForm(), 'form_exercise': ExerciseForm()}
    return render(request, 'api/exercise.html', context)

def exercise_log(request):
    context = {'form_user': ExerciseUserForm(), 'form_exercise': ExerciseForm()}
    return render(request, 'api/exercise.html', context)