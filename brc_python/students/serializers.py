from rest_framework import serializers

from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'last_name', 'first_name', 'nickname', 'pronouns', 'about_me', 'favorite_climb',
                  'goal_climb', 'fun_fact', 'email', 'phone', 'city', 'state']