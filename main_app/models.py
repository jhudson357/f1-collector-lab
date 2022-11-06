from django.db import models
from django.urls import reverse

# Create your models here.
class Team(models.Model):
  name = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  constructors_championships = models.IntegerField()
  drivers_championships = models.IntegerField()
  race_wins = models.IntegerField()

  def __str__(self):
    return self.name