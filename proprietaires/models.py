from django.db import models

class Proprietaire(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    adresse = models.CharField(max_length=50)
    code_postal = models.CharField(max_length=5)
    ville = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nom} {self.prenom}"
