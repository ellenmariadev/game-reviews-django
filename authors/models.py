from django.contrib.auth.models import User
from django.db import models

from games.models import Games, List

# Create your models here.

class Profile (models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    favourite = models.ManyToManyField(Games, default='', blank=True)
    my_lists = models.ManyToManyField(List, default='', blank=True)

