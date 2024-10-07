from rest_framework import viewsets
from.models import *
from .serializers import PerevalSerializer


class PerevalViewset(viewsets.ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer
