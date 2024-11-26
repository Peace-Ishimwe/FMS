# user_management/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages
from .forms import UserCreationForm, UserUpdateForm
from authentication.models import CustomUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomUserSerializer
from authentication.models import CustomUser


class UserListView(APIView):
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@login_required
def user_list(request):
    if request.user.role != 'Admin':
        return HttpResponseForbidden("You do not have permission to access this page.")

    users = CustomUser.objects.all()
    return render(request, 'user_list.html', {'users': users})


@login_required
def user_create(request):
    if request.user.role != 'Admin':
        return HttpResponseForbidden("You do not have permission to create a user.")

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User created successfully.")
            return redirect('user_management:user_list')
    else:
        form = UserCreationForm()
    return render(request, 'user_form.html', {'form': form, 'title': 'Create User'})


@login_required
def user_update(request, user_id):
    if request.user.role != 'Admin':
        return HttpResponseForbidden("You do not have permission to update a user.")

    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "User updated successfully.")
            return redirect('user_management:user_list')
    else:
        form = UserUpdateForm(instance=user)
    return render(request, 'user_form.html', {'form': form, 'title': 'Edit User'})


@login_required
def user_delete(request, user_id):
    if request.user.role != 'Admin':
        return HttpResponseForbidden("You do not have permission to delete a user.")

    user = get_object_or_404(CustomUser, id=user_id)
    user.delete()
    messages.success(request, "User deleted successfully.")
    return redirect('user_management:user_list')
