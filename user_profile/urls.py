from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_view, name='profile_view'),
    path('edit/', views.edit_profile, name='edit_profile'),
    path('change-password/', views.change_password, name='change_password'),
    path('delete-account/', views.delete_account, name='delete_account'),
]