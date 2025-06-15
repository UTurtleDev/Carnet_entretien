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

class Vehicule(models.Model):
    marque = models.CharField(max_length=50)
    modele = models.CharField(max_length=50)
    annee = models.IntegerField()
    annee_achat = models.IntegerField()
    kilometrage_achat = models.IntegerField()
    couleur = models.CharField(max_length=50)
    immatriculation = models.CharField(max_length=9)
    chevaux_fiscaux = models.IntegerField()
    chevaux_din = models.IntegerField()
    carburant = models.CharField(max_length=50, choices=ChoixCarburant.choices)
    transmission = models.CharField(max_length=50, choices=ChoixTransmission.choices)
    proprietaire = models.ForeignKey(Proprietaire, on_delete=models.CASCADE)
    photo = models.ImageField()

    def __str__(self):
        return f"{self.marque} {self.modele}"
