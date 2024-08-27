from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Nota
from .serializers import NotaSerializer



def hello_world(request):
    return HttpResponse("Hello, World!")

class NotaViewSet(viewsets.ModelViewSet):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer

    @action(detail=False, methods=['delete'])
    def delete_all(self, request):
        Nota.objects.all().delete()
        return Response({"message": "All notes have been deleted."}, status=status.HTTP_204_NO_CONTENT)