from django.urls import path

from . import views

urlpatterns = [path('', views.index, name='SECRET NUMBER 1 ;O')]
## urlpatterns = [path('/cum', views.index, name='SECRET CUM ;O')]