from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name

class Games(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    slug = models.SlugField()
    release_date = models.DateField(null=True, blank=True)
    publisher = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='games/covers/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    genre = models.ManyToManyField(Genre)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.title


class ReviewRating(models.Model):
    game = models.ForeignKey(Games, on_delete=models.CASCADE)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )


class List(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    games = models.ManyToManyField(Games)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.title

