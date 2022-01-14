from django import urls
from django.urls import path
from . import views



urlpatterns = [

  path('user_detail', views.UserDetail, name='UserDetail'),
  path('libros_list', views.LibrosList, name='LibrosList'),
]