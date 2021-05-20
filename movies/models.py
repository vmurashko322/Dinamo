from django.db import models

# Create your models here.
from django.urls import reverse


class Director_by(models.Model):
    name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('last_name',)
        verbose_name = 'Режиссер'
        verbose_name_plural = 'Режиссёры'

    def __str__(self):
        return self.name


class Genre(models.Model):
    title = models.CharField(max_length=150, unique=True, db_index=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movies:movie_list_by_genre', args=[self.slug])


class Movie(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    directors_by = models.ManyToManyField('Director_by')
    genres = models.ManyToManyField('Genre')
    date_published = models.IntegerField()
    images = models.ImageField(upload_to='album/%Y/%m/%d')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    class Meta:
        ordering = ('title',)
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movies:movie_detail', args=[self.id, self.slug])
