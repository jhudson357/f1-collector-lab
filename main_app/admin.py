from django.contrib import admin
from .models import Team, Driver, Position

# Register your models here.
admin.site.register(Team)
admin.site.register(Driver)
admin.site.register(Position)