from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls import include

from rest_framework import routers
from .views import ProductAPIView

urlpatterns = [
    path('products', ProductAPIView.as_view())
    # path('products', views.products, name='products')
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
