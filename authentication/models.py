from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

# Create your models here.
class Pengguna(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = CountryField()

    def __str__(self):
        return self.user.username + " pengguna PacilFlix"