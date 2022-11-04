from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

class Team:
  def __init__(self, name, location, constructors_championships, drivers_championships, race_wins):
    self.name = name
    self.location = location
    self.constructors_championships = constructors_championships
    self.drivers_championships = drivers_championships
    self.race_wins = race_wins

teams = [
  Team('Red Bull Racing', 'Milton Keynes, England, UK', 5, 6, 91),
  Team('Mercedes-AMG Petronas F1 Team', 'Brackley, England, UK', 8, 9, 124),
  Team('Scuderia Ferrari', 'Maranello, Province of Modena, Italy', 16, 15, 241),
  Team('Mclaren F1 Team', 'Mclaren Technology Centre, Woking, Surrey, England, UK', 8, 12, 183)
]

def home(request):
  return HttpResponse('<h1>F1 Collector</h1>')

def about(request):
  return render(request, 'about.html')

def teams_index(request):
  return render(request, 'teams/index.html', { 'teams': teams })
