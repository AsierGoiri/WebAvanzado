from django.db import models
from django.contrib.auth.models import User

from biblioapp.models import Libro

# Create your models here.
class Comentario(models.Model):
    usuario = models.CharField(max_length=25)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, null=True)
    comentario = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.usuario)