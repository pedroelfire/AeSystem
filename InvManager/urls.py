from django.urls import path, include
from rest_framework import routers
from .views import *

router =  routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r"moves", MovementViewSet)

urlpatterns = [
    path("manage/", include(router.urls)),
]
