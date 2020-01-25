from django.db import models


def photo_path(instance, filename):
    """Returns the path for saving profile photos"""
    print('profile_photos/{}.{}'.format(instance.id, filename.split('.')[-1]))
    return 'profile_photos/{}.{}'.format(instance.id, filename.split('.')[-1])


class Student(models.Model):
    """This model represents a student profile in the database."""
    last_name = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)
    nickname = models.CharField(max_length=128, null=True, blank=True)
    pronouns = models.CharField(max_length=128, null=True, blank=True)

    photo = models.ImageField(upload_to='profile_photos/', null=True)

    about_me = models.TextField(null=True, blank=True)
    favorite_climb = models.TextField(null=True, blank=True)
    goal_climb = models.TextField(null=True, blank=True)
    fun_fact = models.TextField(null=True, blank=True)

    email = models.EmailField(max_length=256)
    phone = models.CharField(max_length=20)
    street_address = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    state = models.CharField(max_length=128)
    zip = models.CharField(max_length=128)

    insurance_carrier = models.CharField(max_length=128)
    emergency_contact = models.CharField(max_length=128)
    emergency_contact_phone = models.CharField(max_length=128)

    @property
    def name(self):
        """Returns the full name of a student as a string"""
        return '{} {}'.format(self.first_name, self.last_name)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['last_name']
