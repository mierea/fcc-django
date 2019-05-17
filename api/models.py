from django.db import models
from django.core.validators import URLValidator
from django.utils import timezone

# Create your models here.
class Shorturl(models.Model):
    original_url = models.CharField(max_length=200,validators=[URLValidator()])

class User(models.Model):
    username = models.CharField(max_length=100, unique=True,error_messages={'unique':"username taken."})

class Exercise(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=False)
    description = models.CharField(max_length=200, null=False)
    duration = models.IntegerField(null=False)
    date = models.DateField(default=timezone.now, null=False)

