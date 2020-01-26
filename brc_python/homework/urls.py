from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeworkList.as_view()),
]
