from multiprocessing import context
from django.db import models
from django.db.models.query_utils import Q
from django.shortcuts import redirect, render

from comentarios.models import Comentario
from .models import *
from .forms import *
import requests


from django.http.response import HttpResponse
import json
from django.contrib import messages
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.


def Index(request):

    categorias = Categoria.objects.all()
    libros = Libro.objects.all()
    context = {'categorias': categorias, 'libros': libros}

    return render(request, 'index.html', context)


def Marvel(request):

    params = {'ts': 1000, 'apikey': '4fbcd571ae15fe44864b8767aeacc606',
        'hash': '89a881c2372d04841a3187b9b688cbbe'}
    response = requests.get(
        'https://gateway.marvel.com/v1/public/comics', params=params)
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

    context = {'book': book, 'coments': coments, 'form': form}

    return render(request, 'bookDetail.html', context)


def Reservar(request):

    return request


def MisReservas(request):

    reservas = Reserva.objects.filter(user=request.user)
    context = {'reservas': reservas}

    return render(request, 'mis_reservas.html', context)


@login_required
def processOrder(request):

    # cargamos los datos necesarios para realizar el pedido
    data = json.loads(request.body)
    BookId = data['bookid']

    # comprobamos por pantalla que coge bien los datos
    print('Bookid:', BookId)
    libroId = Libro.objects.get(id=BookId)



    print('Llega al pedido')

    print('Pedido de: ', request.user)

    print('LLega hasta el order')
    try:
        Reserva.objects.create(
            user = request.user,
            libro = libroId,
        )
        
        messages.success(request, 'Pedido realizado correctamente.')

    except Exception as e:
        messages.warning(request, 'Error!,', e)
        print('Error en el procesamiento del pedido:', e)


 



    return HttpResponse(request) 

