from django.db import models
from proprietaires.models import Proprietaire


class ChoixCarburant(models.TextChoices):
    diesel = 'Diesel'
    essence = 'Essence'
    electrique = 'Electrique'
    hybride = 'Hybride'

class ChoixTransmission(models.TextChoices):
    manuelle = 'Manuelle'
    automatique = 'Automatique'

class Vehicules(models.Model):
    marque = models.CharField(max_length=50)
    modele = models.CharField(max_length=50)
    annee = models.DateField()
    kilometrage = models.IntegerField(blank=True, null=True)
    annee_achat = models.DateField()
    kilometrage_achat = models.IntegerField()
    couleur = models.CharField(max_length=50)
    immatriculation = models.CharField(max_length=9)
    chevaux_fiscaux = models.IntegerField()
    chevaux_din = models.IntegerField()
    carburant = models.CharField(max_length=50, choices=ChoixCarburant.choices, blank=True, null=True)
    transmission = models.CharField(max_length=50, choices=ChoixTransmission.choices, blank=True, null=True)
    proprietaire = models.ForeignKey(Proprietaire, on_delete=models.CASCADE)
    facture = models.ImageField(upload_to='factures', blank=True, null=True)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.marque} {self.modele}"
    
    @property
    def kilometrage_separator(self):
        return f"{self.kilometrage:,.0f}".replace(',', ' ')
    
    class Meta:
        verbose_name = "Véhicule"
        verbose_name_plural = "Véhicules"
