from sre_parse import State
from django.contrib import admin
from .models import City, User
from .models import Event
from .models import State
# Register your models here.

admin.site.register(User)
admin.site.register(Event)
admin.site.register(City)
admin.site.register(State)