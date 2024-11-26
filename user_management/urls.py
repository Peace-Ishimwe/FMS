# user_management/urls.py
from django.urls import path
from . import views
from .views import UserListView

app_name = 'user_management'

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('create/', views.user_create, name='user_create'),
    path('<int:user_id>/edit/', views.user_update, name='user_update'),
    path('<int:user_id>/delete/', views.user_delete, name='user_delete'),
    path('all', UserListView.as_view(), name='user-list-api'),
]