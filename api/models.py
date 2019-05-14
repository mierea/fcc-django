from django.db import models
from django.core.validators import URLValidator

# Create your models here.
class Shorturl(models.Model):
    original_url = models.TextField(validators=[URLValidator()])