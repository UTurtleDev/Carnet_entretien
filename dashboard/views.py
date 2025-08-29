from django.shortcuts import render
from django.views.generic import ListView

from vehicules.models import Vehicules  

# Create your views here.
def dashboard(request):
    return render(request, 'pages/dashboard/dashboard.html')

class dashboardView(ListView):
    model = Vehicules
    template_name = 'pages/dashboard/dashboard.html'
    context_object_name = 'vehicules'
