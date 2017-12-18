from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django_countries.widgets import CountrySelectWidget
from django_countries import countries


class LoginForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=('username','password','first_name','last_name','email',)





class RegistrationForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('designation','organisation','gender',)
        widgets = {'country': CountrySelectWidget()}







class ImageUpload(forms.ModelForm):
    class Meta:
        model = Profile
        fields =('profile_image',)





class Follow(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('followed_by',)


