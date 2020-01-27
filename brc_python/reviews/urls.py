from django.urls import path
from . import views


urlpatterns = [
    path('skills_night/', views.SkillsNightReviewList.as_view()),
    path('skills_night/<int:pk>', views.SkillsNightReviewDetail.as_view()),
    path('leavenworth/', views.LeavenworthReviewList.as_view()),
    path('leavenworth/<int:pk>', views.LeavenworthReviewDetail.as_view()),
    path('squamish1/', views.Squamish1ReviewList.as_view()),
    path('squamish1/<int:pk>', views.Squamish1ReviewDetail.as_view()),
    path('squamish2/', views.Squamish2ReviewList.as_view()),
    path('squamish2/<int:pk>', views.Squamish2ReviewDetail.as_view()),
    path('grad_climb/', views.GradClimbReviewList.as_view()),
    path('grad_climb/<int:pk>', views.GradClimbReviewDetail.as_view()),
    path('instructor_review/', views.InstructorReviewList.as_view()),
    path('instructor_review/<int:pk>', views.InstructorReviewDetail.as_view()),
]
