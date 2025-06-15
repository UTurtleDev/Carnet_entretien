from django.db import models
from vehicules.models import Vehicule

# Create your models here.
class Entretien(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    date = models.DateField()
    kilometrage = models.IntegerField()
    type_entretien = models.TextField()
    facture = models.ImageField(upload_to='factures')
    montant = models.DecimalField(max_digits=10, decimal_places=2)   

    def __str__(self):
        return f"{self.vehicule} - {self.date}"
    
    #Montant formaté en euros avec espace en séparateur de milliers et virgule en séparateur de decimal
    def montant_formate(self):
        return f"{self.montant:,.2f} €".replace(",", " ").replace(".", ",")

        