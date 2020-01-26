from django.db import models
from django.contrib.postgres.fields import ArrayField


class Outing(models.Model):
    title = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    start_date = models.DateField()
    end_date = models.DateField()
    objectives = ArrayField(models.CharField(max_length=500))
    description = models.TextField()
    itinerary = models.TextField()
    campground = models.CharField(max_length=300, null=True, blank=True)
    campsite = models.CharField(max_length=300, null=True, blank=True)
    camping_location_url = models.URLField(null=True, blank=True)
    camping_checkin_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title


class Lecture(models.Model):
    number = models.IntegerField(primary_key=True)
    topic = models.CharField(max_length=250)
    time = models.DateTimeField()
    location = models.CharField(max_length=250)
    presentation_file = models.URLField(null=True, blank=True)
    location_link = models.URLField(null=True, blank=True)
    potluck_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return 'Lecture ' + str(self.number)

