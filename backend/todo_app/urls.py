from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('categories', CategoryViewSet,basename='category')
router.register('todos', TodoViewSet, basename='todo')

urlpatterns = [
    path('', include(router.urls)),
]