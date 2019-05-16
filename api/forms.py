from django import  forms
from .models import Shorturl, User, Exercise


class ShorturlForm(forms.ModelForm):

    class Meta:
        model = Shorturl
        fields = ('original_url',)


class MetadataForm(forms.Form):
    file = forms.FileField()

class ExerciseUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username',)



class ExerciseForm(forms.ModelForm):

    class Meta:
        model = Exercise
        fields = ('user', 'description', 'duration', 'date')