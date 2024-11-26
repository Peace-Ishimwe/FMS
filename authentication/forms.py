from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email',
                  'phone', 'province', 'sector')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'block w-full p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500'}),
            'last_name': forms.TextInput(attrs={'class': 'block w-full p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500'}),
            'email': forms.EmailInput(attrs={'class': 'block w-full p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500'}),
            'phone': forms.TextInput(attrs={'class': 'block w-full p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500'}),
            'province': forms.Select(attrs={'class': 'block w-full p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500'}),
            'sector': forms.Select(attrs={'class': 'block w-full p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500'}),
            'password1': forms.PasswordInput(attrs={'class': 'block w-full p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500'}),
            'password2': forms.PasswordInput(attrs={'class': 'block w-full p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500'}),
        }


class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'class': 'bloc kw-full p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'block w-full p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500'}))
