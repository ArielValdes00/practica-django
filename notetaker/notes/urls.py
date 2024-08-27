from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NotaViewSet
from .views import hello_world

router = DefaultRouter()
router.register(r'notas', NotaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('hello/', hello_world, name='hello_world'),
]
