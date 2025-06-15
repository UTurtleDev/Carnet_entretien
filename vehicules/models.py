from django.db import models
from proprietaires.models import Proprietaire

<<<<<<< HEAD
=======

class ChoixCarburant(models.TextChoices):
    diesel = 'Diesel'
    essence = 'Essence'
    electrique = 'Electrique'
    hybride = 'Hybride'

class ChoixTransmission(models.TextChoices):
    manuelle = 'Manuelle'
    automatique = 'Automatique'

>>>>>>> HEAD@{1}
class Vehicule(models.Model):
    marque = models.CharField(max_length=50)
    modele = models.CharField(max_length=50)
    annee = models.IntegerField()
<<<<<<< HEAD
    annee_achat = models.DateField()
=======
    annee_achat = models.IntegerField()
>>>>>>> HEAD@{1}
    kilometrage_achat = models.IntegerField()
    couleur = models.CharField(max_length=50)
    immatriculation = models.CharField(max_length=9)
    chevaux_fiscaux = models.IntegerField()
    chevaux_din = models.IntegerField()
<<<<<<< HEAD
=======
    carburant = models.CharField(max_length=50, choices=ChoixCarburant.choices)
    transmission = models.CharField(max_length=50, choices=ChoixTransmission.choices)
>>>>>>> HEAD@{1}
    proprietaire = models.ForeignKey(Proprietaire, on_delete=models.CASCADE)
    photo = models.ImageField()

    def __str__(self):
        return f"{self.marque} {self.modele}"
