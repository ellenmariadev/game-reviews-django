from django.contrib import admin

from .models import Games, Genre, List, ReviewRating, Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    ...

class ListAdmin(admin.ModelAdmin):
    ...

class GenreAdmin(admin.ModelAdmin):
    ...

class ReviewRatingAdmin(admin.ModelAdmin):
    ...


@admin.register(Games)
class GamesAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'publisher'
    list_display_links = 'title', 'publisher'
    search_fields = 'id', 'title', 'description', 'slug', 'publisher'
    list_filter = 'genre', 'publisher'
    ordering = ['title']
    prepopulated_fields = {
        "slug": ['title']
    }

@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'author'
    list_display_links = 'title', 'author'
    search_fields = 'id', 'title', 'description', 'slug', 'author'
    list_filter = 'games', 'author'
    ordering = ['title']

admin.site.register(Genre, GenreAdmin)
admin.site.register(ReviewRating, ReviewRatingAdmin)
admin.site.register(Profile, ProfileAdmin)
