from django.db import models

# Create your models here.

# Creeation des models a qui on des relations
class Date(models.Model):
    year = models.IntegerField()


class Genre(models.Model):
    name = models.CharField(max_length=50)


class Countrie(models.Model):
    name = models.CharField(max_length=50)
    

class Director(models.Model):
    name = models.CharField(max_length=100)
    

class Actor(models.Model):
    name = models.CharField(max_length=100)
   
    
 # Creation du models films
class Movie(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    time = models.CharField(max_length=15)
    rating = models.IntegerField()
    year = models.ForeignKey(Date, on_delete=models.CASCADE)
    countries = models.ManyToManyField(Countrie, related_name="movies", blank=True)
    directors = models.ManyToManyField(Director, related_name="movies", blank=True)
    actors = models.ManyToManyField(Actor, related_name="movies", blank=True)