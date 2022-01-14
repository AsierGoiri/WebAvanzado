from django import urls
from django.urls import path
from . import views



urlpatterns = [

    path('', views.Index, name='Index'),
    path('marvelApi/', views.Marvel, name='Marvel'),
    path('comicCharacters/<int:pk>', views.Characters, name='Characters'),
    path('addBook/', views.addBook, name='addBook'),
    path('book/<int:pk>', views.Book, name='Book'),
]