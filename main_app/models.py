from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

POSITIONS = (
  ('A', 'Aero'),
  ('D', 'Design'),
  ('F', 'Finance'),
  ('H', 'HR'),
  ('M', 'Marketing/Media'),
  ('R', 'Race Team')
)

# Create your models here.
class Position(models.Model):
  name = models.CharField(max_length=50)
  department = models.CharField(
    max_length=1,
    choices=POSITIONS,
    default=POSITIONS[0][0]
  )

  def __str__(self):
    return f'{self.name} - {self.get_department_display()}'
  
  def get_absolute_url(self):
    return reverse('positions_detail', kwargs={'pk': self.id})

class Team(models.Model):
  name = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  constructors_championships = models.IntegerField()
  drivers_championships = models.IntegerField()
  race_wins = models.IntegerField()
  positions = models.ManyToManyField(Position)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
      return reverse('teams_detail', kwargs={'team_id': self.id})
  
  def drivers_selected(self):
    return self.driver_set.all().count() >= 2
  
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
