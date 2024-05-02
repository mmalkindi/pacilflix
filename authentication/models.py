from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField

# Create your models here.
class Pengguna(models.Model):
    country = CountryField()

    def __str__(self):
        return self.username + " pengguna PacilFlix"