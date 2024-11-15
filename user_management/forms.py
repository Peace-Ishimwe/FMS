# user_management/forms.py
from django import forms
from authentication.models import CustomUser

class UserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'phone', 'province', 'sector', 'role']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded p-2'}),
            'first_name': forms.TextInput(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded p-2'}),
            'last_name': forms.TextInput(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded p-2'}),
            'phone': forms.TextInput(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded p-2'}),
            'province': forms.Select(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded p-2'}),
            'sector': forms.Select(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded p-2'}),
            'role': forms.Select(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded p-2'}),
        }

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'phone', 'province', 'sector', 'role']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control mt-1 block w-full border border-gray-300 rounded p-2'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control mt-1 block w-full border border-gray-300 rounded p-2'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control mt-1 block w-full border border-gray-300 rounded p-2'}),
            'phone': forms.TextInput(attrs={'class': 'form-control mt-1 block w-full border border-gray-300 rounded p-2'}),
            'province': forms.TextInput(attrs={'class': 'form-select mt-1 block w-full border border-gray-300 rounded p-2'}),
            'sector': forms.Select(attrs={'class': 'form-select mt-1 block w-full border border-gray-300 rounded p-2'}),
            'role': forms.Select(attrs={'class': 'form-select mt-1 block w-full border border-gray-300 rounded p-2'}),
        }