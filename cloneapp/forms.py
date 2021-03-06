from django import forms
from django.contrib.auth.models import User
from .models import Lister, Item


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

class ListerForm(forms.ModelForm):
    class Meta:
        model = Lister
        fields = ['e_mail', 'city']


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'price', 'description']
