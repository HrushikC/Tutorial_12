from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Account


# classes 1 & 2 are part of registering
# classes 3 & 4 are part of updating account


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class AccountRegisterForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ['is_tutor']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfilePicUpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['is_tutor', 'image']
