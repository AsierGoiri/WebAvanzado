from django.db import models

from biblioteca.settings import DATABASES
from django.contrib.auth.models import User

# Create your models here.
class Autor(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name


class Categoria(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name



class Libro(models.Model):
    titulo = models.CharField(max_length=25)
    sipnosis = models.TextField(max_length=100, null=True, blank= True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, null=True)
       
   
    def __str__(self):
        return self.titulo

class Reserva(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    libro = models.ForeignKey(Libro,on_delete=models.CASCADE, default=1)

    def __str__(self):
        return str(self.id)
