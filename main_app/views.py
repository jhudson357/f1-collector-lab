from django.shortcuts import render
from .models import Team

# Create your views here.

# teams = [
#   Team('Red Bull Racing', 'Milton Keynes, England, UK', 5, 6, 91),
#   Team('Mercedes-AMG Petronas F1 Team', 'Brackley, England, UK', 8, 9, 124),
#   Team('Scuderia Ferrari', 'Maranello, Province of Modena, Italy', 16, 15, 241),
#   Team('Mclaren F1 Team', 'Mclaren Technology Centre, Woking, Surrey, England, UK', 8, 12, 183)
# ]

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def teams_index(request):
  teams = Team.objects.all()
  return render(request, 'teams/index.html', { 'teams': teams })
