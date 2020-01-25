from django.db import models



class Homework(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    lecture = models.ForeignKey('meetings.lecture', models.SET_NULL, null=True)

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['due_date']
