from django.urls import path
from . import views

urlpatterns = [
    # path core
    path('', views.contact, name='contact'),
]