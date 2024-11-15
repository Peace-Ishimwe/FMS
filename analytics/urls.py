# analytics/urls.py
from django.urls import path
from . import views

app_name = 'analytics'

urlpatterns = [
    path('', views.funding_analytics, name='funding_analytics'),
]