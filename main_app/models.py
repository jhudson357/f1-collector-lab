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

  def get_absolute_url(self):
      return reverse('teams_detail', kwargs={'team_id': self.id})
  
class Driver(models.Model):
  name = models.CharField(max_length=100)
  age = models.IntegerField()
  nationality = models.CharField(max_length = 20)
  start_year = models.IntegerField()
  wins = models.IntegerField()
  championships = models.IntegerField()
  team = models.ForeignKey(Team, on_delete=models.CASCADE)

  def __str__(self):
    return self.name