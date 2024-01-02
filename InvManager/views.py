from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from .serializer import *

class ProductViewSet(viewsets.ModelViewSet):
   queryset = Product.objects.all()
   serializer_class = ProductSerializer
    