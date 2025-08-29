from django.db import models
from django.core.exceptions import ValidationError
from vehicules.models import Vehicules

# Create your models here.
def validateur_extentions(value):
    if not value.name.endswith('.pdf'):
        raise ValidationError('Le fichier doit avoir l\'extension .pdf')

class Entretien(models.Model):
    vehicule = models.ForeignKey(Vehicules, on_delete=models.CASCADE)
    date = models.DateField()
    kilometrage = models.IntegerField()
    type_entretien = models.TextField()
    facture = models.FileField(upload_to='factures', validators = [validateur_extentions])
    montant = models.DecimalField(max_digits=10, decimal_places=2)   

    def __str__(self):
        return f"{self.date} - {self.vehicule} - {self.type_entretien}"
    
    #Montant formaté en euros avec espace en séparateur de milliers et virgule en séparateur de decimal
    def montant_formate(self):
        return f"{self.montant:,.2f} €".replace(",", " ").replace(".", ",")

        