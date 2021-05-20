from django.contrib import admin
from .models import Genre, Director_by, Movie


class Director_byAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Director_by,Director_byAdmin)


class GenreAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Genre, GenreAdmin)


class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'date_published', 'images']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Movie, MovieAdmin)
