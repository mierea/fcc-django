from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('', views.api_list, name='api_list'),
    path('timestamp/', views.timestamp, name='timestamp'),
    path('timestamp/<int:date_number>', views.utc_string, name='utc_string'),
]
