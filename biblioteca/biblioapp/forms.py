from django import forms

from comentarios.models import Comentario
from .models import *


class AddBook(forms.ModelForm):

    titulo = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    sipnosis = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Libro
        fields = ('titulo', 'sipnosis', 'categoria', 'autor')

    widgets = {

        'categoria': forms.Select(attrs={'class': 'form-control '}),
        'autor': forms.Select(attrs={'class': 'form-control '}),

    }


class AddComment(forms.ModelForm):

    comentario = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Comentario
        fields = ['usuario', 'comentario', 'libro']

    widgets = {
        'usuario': forms.NumberInput(attrs={'class': 'form-control', 'value': '', 'id': 'usuario', 'type': 'hidden'}),
        'libro': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'libro', 'type': 'hidden'}),
    }
