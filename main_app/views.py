from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Team, Position
from .forms import DriverForm

# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def teams_index(request):
  teams = Team.objects.filter(user=request.user)
  return render(request, 'teams/index.html', { 'teams': teams })

@login_required
def teams_detail(request, team_id):
  team = Team.objects.get(id=team_id)
  positions_team_doesnt_have = Position.objects.exclude(id__in = team.positions.all().values_list('id'))
  driver_form = DriverForm()
  return render(request, 'teams/detail.html', { 
    'team': team,
    'driver_form': driver_form,
    'positions': positions_team_doesnt_have
  })

class CreateTeam(LoginRequiredMixin, CreateView):
  model = Team
  fields = ['name', 'location', 'constructors_championships', 'drivers_championships', 'race_wins']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class TeamUpdate(LoginRequiredMixin, UpdateView):
  model = Team
  fields = ['name', 'location', 'constructors_championships', 'drivers_championships', 'race_wins']

class TeamDelete(LoginRequiredMixin, DeleteView):
  model = Team
  success_url = '/teams/'

@login_required
def add_driver(request, team_id):
  form = DriverForm(request.POST)
  if form.is_valid():
    new_driver = form.save(commit=False)
    new_driver.team_id = team_id
    new_driver.save()
  return redirect('teams_detail', team_id=team_id)

class PositionCreate(LoginRequiredMixin, CreateView):
  model = Position
  fields = '__all__'

class PositionList(LoginRequiredMixin, ListView):
  model = Position

class PositionDetail(LoginRequiredMixin, DetailView):
  model = Position

class PositionUpdate(LoginRequiredMixin, UpdateView):
  model = Position
  fields = '__all__'

class PositionDelete(LoginRequiredMixin, DeleteView):
  model = Position
  success_url = '/positions/'

@login_required
def assoc_position(request, team_id, position_id):
  Team.objects.get(id=team_id).positions.add(position_id)
  return redirect('teams_detail', team_id=team_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('teams_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)