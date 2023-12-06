from django.shortcuts import render

# Create your views here.
from .models import Client
from rest_framework import viewsets
from .serializer import ClientSerializer

# Após o comentario "# Create your views here." e crie as views "Client".

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer  

