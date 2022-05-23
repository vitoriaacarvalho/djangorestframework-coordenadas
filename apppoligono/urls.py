from django.urls import path, include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'linhas', lineViewSet, basename='linhas')
router.register(r'ponto', pointViewSet, basename='ponto')
router.register(r'poligono', polygonViewSet, basename='poligono')
router.register(r'Image', imageViewSet, basename='image')


urlpatterns = router.urls

