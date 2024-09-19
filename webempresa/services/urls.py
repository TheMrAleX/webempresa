from django.urls import path
from . import views

urlpatterns = [
    # path core
    path('', views.services, name='services'),
]