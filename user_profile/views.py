from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import ProfileForm, UserForm
from authentication.models import CustomUser

# View to display the profile page
@login_required
def profile_view(request):
    user = request.user
    user_profile = CustomUser.objects.get(email=user)
    
    return render(request, 'profile_view.html', {'user': user, 'user_profile': user_profile})

# View to edit profile
@login_required
def edit_profile(request):
    user = request.user
    user_profile = CustomUser.objects.get(email=user)
    
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, instance=user_profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile_view')
    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=user_profile)
    
    return render(request, 'edit_profile.html', {'user_form': user_form, 'profile_form': profile_form})


# View to change password
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile_view')
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'change_password.html', {'form': form})

# View to delete account
@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        return redirect('home')
    return render(request, 'delete_account.html')