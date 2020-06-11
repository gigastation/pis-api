from rest_framework import generics
from .models import Product
from .serializer import ProductSerializer


class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
