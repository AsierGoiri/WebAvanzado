from pyexpat import model
from django.db.models.base import ModelState
from rest_framework import serializers
from biblioapp.models import Libro, models
from django.contrib.auth.models import User






class LibroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Libro
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'