from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from .serializers import *
from django.contrib.auth.models import User
from biblioapp.models import *
# Create your views here.



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def UserDetail(request):
	
    tokeeeen = request.META.get('HTTP_AUTHORIZATION')
    print(tokeeeen)
    # Recortamos el token para quedarnos con lo que realmente queremos
    token = tokeeeen[6:]
    print(token)
    # Consultamos que token se ha usado en nuestra bd
    user_Token = Token.objects.get(key=token)
    # Consultamos a que usuario pertenece ese Token 
    user_request = User.objects.get(id=user_Token.user.id)
    print('User:', user_request)

    serializer = UserSerializer(user_request, many=False)

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def LibrosList(request):
	
    libros = Libro.objects.all()

    serializer = LibroSerializer(libros, many=True)

    return Response(serializer.data)



