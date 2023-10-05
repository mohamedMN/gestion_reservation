
from django.contrib import admin

# Register your models here.

#appel a model de utilisateur
from .models import *

admin.site.register(Utilisateur)

admin.site.register(Salle)

admin.site.register(Reservation)

admin.site.register(Place)
