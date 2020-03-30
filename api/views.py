# from django.shortcuts import render
# from django.http import HttpResponse
from .models import Product
# from django.core import serializers
from rest_framework import viewsets, filters
from .serializer import ProductSerializer


# def index(request):
#     return HttpResponse("", content_type="application/json")


# def products(request):
#     products = serializers.serialize('json', Product.objects.all())
#     return HttpResponse(products, content_type="application/json")

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
