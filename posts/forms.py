from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.admin import widgets
from .models import Comments


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    birthday = forms.DateField(initial='month/day/year')
    country = forms.CharField()
    city = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'birthday',
        		  'country', 'city')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comments_text']