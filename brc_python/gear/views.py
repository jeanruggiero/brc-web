from rest_framework import viewsets

from .serializers import GearSerializer
from .models import Gear


class GearView(viewsets.ModelViewSet):
    serializer_class = GearSerializer
    queryset = Gear.objects.all()
