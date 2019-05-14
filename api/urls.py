from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('', views.api_list, name='api_list'),
    path('timestamp/', views.timestamp, name='timestamp'),
    path('timestamp/<int:date_number>', views.utc_string, name='utc_string'),
    path('timestamp/<int:uyear>-<int:umonth>-<int:uday>', views.day_string, name="day_string"),
    path('header_parser/', views.header_parser, name='header_parser'),
    path('header_parser/whoami', views.whoami, name='whoami'),
    path('shorturl/', views.shorturl, name='shorturl'),
    path('shorturl/new', views.shorturl_new, name='shorturl_new'),
    path('shorturl/<int:pk>', views.shorturl_redirect, name='shorturl_redirect'),
    path('metadata/', views.file_metadata, name='file_metadata'),
]
