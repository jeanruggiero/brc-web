from django.db import models


class Gear(models.Model):
    name = models.CharField(max_length=128)
    quantity = models.IntegerField()
    description = models.TextField()
    recommendation = models.CharField(max_length=250, null=True, blank=True)
    recommendation_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'gear'

