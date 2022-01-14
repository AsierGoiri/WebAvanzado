from django.urls import path
from django.conf.urls import include
from . import views
from .views import *

urlpatterns = [
    path('login/', views.Login, name='Login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
]
