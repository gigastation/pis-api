from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls import include

from rest_framework import routers
from .views import ProductViewSet

urlpatterns = [
    # path('', views.index, name='index'),
    # path('products', views.products, name='products')
]
router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
