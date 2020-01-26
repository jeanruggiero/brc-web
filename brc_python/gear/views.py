from rest_framework import generics

from .serializers import GearSerializer
from .models import Gear


class GearList(generics.ListAPIView):
    queryset = Gear.objects.all()
    serializer_class = GearSerializer
