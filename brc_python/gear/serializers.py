from rest_framework import serializers
from .models import Gear


class GearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gear
        fields = ('name', 'quantity','description', 'recommendation')
