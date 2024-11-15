from django.urls import path
from . import views

app_name = 'campaigns'

urlpatterns = [
    path('', views.campaign_list, name='campaign_list'),
    path('<int:campaign_id>/', views.campaign_detail, name='campaign_detail'),
    path('create/', views.campaign_create, name='campaign_create'),
    path('<int:campaign_id>/edit/', views.campaign_update, name='campaign_update'),
]
