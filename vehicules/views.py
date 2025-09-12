from django.shortcuts import render
from django.views.generic import DetailView
from datetime import datetime   

from vehicules.models import Vehicules

# Create your views here.


class DetailVehiculesView(DetailView):
    model = Vehicules
    template_name = 'pages/vehicules/detail_vehicule.html'
    context_object_name = 'vehicules'
    ordering = ['marque', 'modele']
