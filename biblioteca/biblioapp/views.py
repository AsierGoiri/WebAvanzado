from django.db import models
from django.db.models.query_utils import Q
from django.shortcuts import redirect, render

from comentarios.models import Comentario
from .models import *
from .forms import *
import requests

# Create your views here.

def Index(request):


    categorias = Categoria.objects.all()
    libros = Libro.objects.all()
    context = {'categorias':categorias, 'libros':libros}

    return render(request, 'index.html', context)


def Marvel(request):

    params = {'ts':1000, 'apikey':'4fbcd571ae15fe44864b8767aeacc606', 'hash':'89a881c2372d04841a3187b9b688cbbe'}
    response = requests.get('https://gateway.marvel.com/v1/public/comics',params=params)
    api = response.json()
    data = api["data"]['results']

    
       
    print('Data:', data)

    context = {"data": data}
    return render(request, 'marvel.html', context)


def Characters(request, pk):

    # params = {'ts':1000, 'apikey':'4fbcd571ae15fe44864b8767aeacc606', 'hash':'89a881c2372d04841a3187b9b688cbbe'}
    # response = requests.get('https://gateway.marvel.com/v1/public/comics/' + pk +'/characters',params=params)
    # api = response.json()
    # data = api["data"]

    # print('Data:', data)

    # context = {"data": data}
    return render(request, 'carrousel.html')



def addBook(request):
    form = AddBook()
    if request.method == 'POST':
        form = AddBook(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Index')

    context = {"form": form}

    return render(request, 'addBook.html', context)





def Book(request, pk):

    book = Libro.objects.get(id=pk)

    coments = Comentario.objects.filter(libro_id=pk)
  

    
    form = AddComment()
    if request.method == 'POST':
        form = AddComment(request.POST)
        if form.is_valid():
            form.save()
            

    context = {'book':book, 'coments':coments, 'form':form}
    
    return render(request, 'bookDetail.html', context )


def Reservar(request):



    return request