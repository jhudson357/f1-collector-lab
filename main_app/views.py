from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Team, Position
from .forms import DriverForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def teams_index(request):
  teams = Team.objects.all()
  return render(request, 'teams/index.html', { 'teams': teams })

def teams_detail(request, team_id):
  team = Team.objects.get(id=team_id)
  driver_form = DriverForm()
  return render(request, 'teams/detail.html', { 
    'team': team,
    'driver_form': driver_form
  })

class CreateTeam(CreateView):
  model = Team
  fields = '__all__'

class TeamUpdate(UpdateView):
  model = Team
  fields = '__all__'

class TeamDelete(DeleteView):
  model = Team
  success_url = '/teams/'

def add_driver(request, team_id):
  form = DriverForm(request.POST)
  if form.is_valid():
    new_driver = form.save(commit=False)
    new_driver.team_id = team_id
    new_driver.save()
  return redirect('teams_detail', team_id=team_id)

class PositionCreate(CreateView):
  model = Position
  fields = '__all__'

class PositionList(ListView):
  model = Position

class PositionDetail(DetailView):
  model = Position

class PositionUpdate(UpdateView):
  model = Position
  fields = '__all__'

class PositionDelete(DeleteView):
  model = Position
  success_url = '/positions/'
