from django.urls import path
from . import views


urlpatterns = [
    path('lectures/', views.LectureList.as_view()),
    path('outings/', views.OutingList.as_view()),
]