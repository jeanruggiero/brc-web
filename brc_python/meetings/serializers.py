from rest_framework import serializers
from .models import Lecture, Outing


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ['number', 'topic', 'time', 'location', 'presentation_file', 'location_link', 'potluck_link']


class OutingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outing
        fields = ['title', 'location', 'start_date', 'end_date', 'objectives', 'description', 'itinerary',
                  'campground', 'campsite', 'camping_location_url', 'camping_checkin_time']
