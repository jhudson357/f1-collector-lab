from django.urls import path
from . import views

urlpatterns = [
  # localhost:8000/
  path('', views.home, name='home'),
  path('about/', views.about, name='about')
]