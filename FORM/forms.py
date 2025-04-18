from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ["username", "email", "phone", "password1", "password2"]