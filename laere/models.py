
from django.db import models



# Create your models here.

class State(models.Model):

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.first_name

class Event(models.Model):
    photo_url = models.CharField(max_length=600,null=True)
    event = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=200)
    dateTime = models.CharField(max_length=200,null=True)
    host= models.CharField(max_length=100)
    location = models.CharField(max_length=200,null=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=800) 
    url = models.CharField(max_length=600,null=True)

    def __str__(self):
        return self.title

#class Ratings(models.Model):
#    rating = models.IntegerChoices()
#    comment = models.CharField(max_length=600)

