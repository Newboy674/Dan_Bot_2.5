from django.urls import path

from . import views

urlpatterns = [path('', views.index, name='Not OG hello')]