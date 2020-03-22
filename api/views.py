from django.shortcuts import render
from django.http import HttpResponse
from api.models import Product
from django.core import serializers



def index(request):
    return HttpResponse("", content_type="application/json")


def products(request):
    products = serializers.serialize('json', Product.objects.all())
    return HttpResponse(products, content_type="application/json")


