from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from authentication.models import CustomUser

# Form to update profile information
class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['phone', 'province', 'sector']

# Form to update user data (name)
class UserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

# Form to change password
class PasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['password']