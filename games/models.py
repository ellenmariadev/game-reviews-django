# from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Avg

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
    genre = models.ManyToManyField(Genre) #-----FIX-----#
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.title
    
    def averageReview(self):
        reviews = ReviewRating.objects.filter(product=self, status=True).aggregate(average=Avg('rating'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
        return avg

class ReviewRating(models.Model):
    game = models.ForeignKey(Games, on_delete=models.CASCADE)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    status = models.BooleanField(default=True)
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

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favourite = models.ManyToManyField(Games)
    my_lists = models.ManyToManyField(List)
