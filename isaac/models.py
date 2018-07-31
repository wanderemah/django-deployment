from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    # create the rship with the User model DO NOT INHERIT
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # additional attributes
    picture = models.ImageField(upload_to='profile_pics')
    portfolio = models.URLField(blank=True)

    def __str__(self):
        return self.user.username
