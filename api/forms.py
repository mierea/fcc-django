from django import  forms
from .models import Shorturl

class ShorturlForm(forms.ModelForm):

    class Meta:
        model = Shorturl
        fields = ('original_url',)

