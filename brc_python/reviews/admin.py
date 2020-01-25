from django.contrib import admin
from .models import LeavenworthReview, SkillsNightReview, Squamish1Review, \
    Squamish2Review, GradClimbReview, InstructorReview


admin.site.register([LeavenworthReview, SkillsNightReview, Squamish1Review,
                     Squamish2Review, GradClimbReview, InstructorReview])
