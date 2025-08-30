from django.shortcuts import render
from django.views.generic import ListView
from datetime import datetime

from vehicules.models import Vehicules  
from entretiens.models import EntretienPlanifie

# Create your views here.
def dashboard(request):
    return render(request, 'pages/dashboard/dashboard.html')

class dashboardView(ListView):
    model = Vehicules
    template_name = 'pages/dashboard/dashboard.html'
    context_object_name = 'vehicules'
    ordering = ['marque', 'modele']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Récupérer tous les entretiens planifiés non effectués
        entretiens_planifies = EntretienPlanifie.objects.filter(effectue=False)
        
        # Fonction pour convertir date_prevue (mm/aa) en date pour le tri
        def date_sort_key(entretien):
            if entretien.date_prevue:
                try:
                    # Convertir "mm/aa" en date (prendre le 1er du mois)
                    mois, annee = entretien.date_prevue.split('/')
                    # Ajouter 2000 si année sur 2 chiffres
                    annee_complete = int('20' + annee) if len(annee) == 2 else int(annee)
                    return datetime(annee_complete, int(mois), 1)
                except (ValueError, IndexError):
                    # En cas d'erreur de format, mettre à la fin
                    return datetime(9999, 12, 31)
            else:
                # Si pas de date, trier par kilométrage (les plus petits d'abord)
                return datetime(2030, 1, 1) if entretien.kilometrage_prevu else datetime(9999, 12, 31)
        
        # Trier les entretiens par date la plus proche
        entretiens_tries = sorted(entretiens_planifies, key=date_sort_key)
        
        context['entretiens_planifies_tries'] = entretiens_tries
        return context
    


