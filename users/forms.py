# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import user  # Use this if not using a custom user model

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User  # Use User here if not using CustomUser
        fields = ['username', 'email', 'password1', 'password2']
