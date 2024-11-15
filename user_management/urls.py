# user_management/urls.py
from django.urls import path
from . import views

app_name = 'user_management'

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('create/', views.user_create, name='user_create'),
    path('<int:user_id>/edit/', views.user_update, name='user_update'),
    path('<int:user_id>/delete/', views.user_delete, name='user_delete'),
]