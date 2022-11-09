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
  # localhost:8000/teams/int:team_id/add_driver
  path('teams/<int:team_id>/add_driver/', views.add_driver, name='add_driver'),
  # localhost:8000/teams/int:team_id/assoc_position/int:position_id
  path('teams/<int:team_id>/assoc_position/<int:position_id>/', views.assoc_position, name='assoc_position'),

  path('positions/create/', views.PositionCreate.as_view(), name='positions_create'),
  path('positions/<int:pk>/', views.PositionDetail.as_view(), name='positions_detail'),
  path('positions/', views.PositionList.as_view(), name='positions_index'),
  path('positions/<int:pk>/update/', views.PositionUpdate.as_view(), name='positions_update'),
  path('positions/<int:pk>/delete/', views.PositionDelete.as_view(), name='positions_delete'),
]