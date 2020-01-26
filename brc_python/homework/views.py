from rest_framework import generics
from datetime import datetime

from .serializers import HomeworkSerializer
from .models import Homework


class HomeworkList(generics.ListAPIView):

    serializer_class = HomeworkSerializer

    def get_queryset(self):
        queryset = Homework.objects.all()

        if self.request.query_params.get('dueAfter'):
            queryset = queryset.filter(due_date__gt=datetime.strptime(
                self.request.query_params.get('dueAfter'), '%Y-%m-%d'))

        if self.request.query_params.get('dueBefore'):
            queryset = queryset.filter(due_date__lt=datetime.strptime(
                self.request.query_params.get('dueBefore'), '%Y-%m-%d'))

        return queryset