from django.shortcuts import render
from django.views.generic import DetailView
from datetime import datetime   

from vehicules.models import Vehicules
from entretiens.models import Entretien


# Create your views here.


class DetailVehiculesView(DetailView):
    model = Vehicules
    template_name = 'pages/vehicules/detail_vehicule.html'
    context_object_name = 'vehicule'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vehicule = self.get_object()
        context['entretiens'] = vehicule.entretiens.all().order_by('-date')
        context['entretiens_planifies'] = vehicule.entretiens_planifies.all().order_by('-date_prevue')
        return context
