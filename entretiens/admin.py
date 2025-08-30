from django.contrib import admin
from .models import Entretien, EntretienPlanifie

# Register your models here.
admin.site.register(Entretien)
admin.site.register(EntretienPlanifie)
