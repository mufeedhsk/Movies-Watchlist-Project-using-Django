from django.db import models

# Create your models here.
class Movies(models.Model):
    movie_image = models.ImageField(upload_to='index')
    movie_rating = models.CharField(max_length=50)
    movie_name = models.CharField(max_length=150)
    movie_genre = models.CharField(max_length=100)

class Thriller(models.Model):
    T_movie_image = models.ImageField(upload_to='thriller')
    T_movie_rating = models.CharField(max_length=50)
    T_movie_name = models.CharField(max_length=150)
    T_movie_genre = models.CharField(max_length=100)

class Horror(models.Model):
    H_movie_image = models.ImageField(upload_to='horror')
    H_movie_rating = models.CharField(max_length=50)
    H_movie_name = models.CharField(max_length=150)
    H_movie_genre = models.CharField(max_length=100)

class Action(models.Model):
    A_movie_image = models.ImageField(upload_to='action')
    A_movie_rating = models.CharField(max_length=50)
    A_movie_name = models.CharField(max_length=150)
    A_movie_genre = models.CharField(max_length=100)    

class Comedy(models.Model):
    C_movie_image = models.ImageField(upload_to='comedy')
    C_movie_rating = models.CharField(max_length=50)
    C_movie_name = models.CharField(max_length=150)
    C_movie_genre = models.CharField(max_length=100)
    