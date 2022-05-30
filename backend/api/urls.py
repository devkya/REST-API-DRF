from rest_framework import routers
from django.urls import path, include
from .views import *

router = routers.DefaultRouter()
router.register(r'peoples', PersonViewSet)
router.register(r'species', SpeciesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
