from django.urls import path
from . import views

urlpatterns = [
  # localhost:8000/
  path('', views.home, name='home'),
  # localhost:8000/about
  path('about/', views.about, name='about'),
  # localhost:8000/teams
  path('teams/', views.teams_index, name='teams_index'),
  # localhost:8000/teams/int:team_id
  path('teams/<int:team_id>/', views.teams_detail, name='teams_detail'),
  # localhost:8000/teams/create
  path('teams/create/', views.CreateTeam.as_view(), name='teams_create'),
  # localhost:8000/teams/int:pk/update
  path('teams/<int:pk>/update/', views.TeamUpdate.as_view(), name='teams_update'),
  # localhost:8000/teams/int:pk/delete
  path('teams/<int:pk>/delete/', views.TeamDelete.as_view(), name='teams_delete'),
]