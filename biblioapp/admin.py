from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Libro)
admin.site.register(Reserva)

# admin.site.register(User, UserAdmin)
