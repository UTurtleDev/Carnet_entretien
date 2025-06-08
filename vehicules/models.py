from django.db import models
from proprietaires.models import proprietaire

class vehicule(models.Model):
    marque = models.CharField(max_length=50)
    modele = models.CharField(max_length=50)
    annee = models.IntegerField()
    annee_achat = models.ImageField()
    kilometrage_achat = models.IntegerField()
    couleur = models.CharField(max_length=50)
    immatriculation = models.CharField(max_length=50)
    chevaux_fiscaux = models.IntegerField()
    chevaux_din = models.IntegerField()
    proprietaire = models.ForeignKey(proprietaire, on_delete=models.CASCADE)
    photo = models.ImageField()

    def __str__(self):
        return f"{self.marque} {self.modele}"
