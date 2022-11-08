from django.forms import ModelForm
from .models import Driver

class DriverForm(ModelForm):
  class Meta:
    model = Driver
    fields = [
      'name',
      'age',
      'nationality',
      'start_year',
      'wins',
      'championships'
    ]