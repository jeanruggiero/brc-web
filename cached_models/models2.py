# from django.db import models
# from django.contrib.auth.models import User
# from django.utils import timezone
#
#
# class Update(models.Model):
#     author = models.ForeignKey(User, models.SET_NULL, null=True)
#     time = models.DateTimeField(default=timezone.now)
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#
#     def __repr__(self):
#         return self.title
