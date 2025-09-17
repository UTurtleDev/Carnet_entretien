from django.db import models
from django.core.exceptions import ValidationError
from proprietaires.models import Proprietaire


def validateur_extensions_document(value):
    extensions_valides = ['.pdf', '.jpg', '.jpeg', '.png', '.doc', '.docx']
    if not any(value.name.lower().endswith(ext) for ext in extensions_valides):
        raise ValidationError('Le fichier doit avoir l\'une des extensions suivantes : .pdf, .jpg, .jpeg, .png, .doc, .docx')


class TypeDocument(models.TextChoices):
    ASSURANCE = 'assurance', 'Assurance'
    CONTROLE_TECHNIQUE = 'controle_technique', 'Contrôle technique'
    CARTE_GRISE = 'carte_grise', 'Carte grise'
    FACTURE_ACHAT = 'facture_achat', 'Facture d\'achat'
    FACTURE_ENTRETIEN = 'facture_entretien', 'Facture d\'entretien'
    AUTRE = 'autre', 'Autre'


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


class Document(models.Model):
    vehicule = models.ForeignKey(Vehicules, on_delete=models.CASCADE, related_name='documents')
    type_document = models.CharField(max_length=50, choices=TypeDocument.choices)
    nom = models.CharField(max_length=200, help_text="Nom du document")
    fichier = models.FileField(upload_to='documents/', validators=[validateur_extensions_document])
    date_document = models.DateField(blank=True, null=True, help_text="Date du document")
    date_expiration = models.DateField(blank=True, null=True, help_text="Date d'expiration (si applicable)")
    date_upload = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True, help_text="Notes ou commentaires")
    
    def __str__(self):
        return f"{self.vehicule} - {self.get_type_document_display()} - {self.nom}"
    
    @property
    def est_expire(self):
        if self.date_expiration:
            from django.utils import timezone
            return self.date_expiration < timezone.now().date()
        return False
    
    @property 
    def expire_bientot(self):
        if self.date_expiration:
            from django.utils import timezone
            from datetime import timedelta
            return self.date_expiration <= (timezone.now().date() + timedelta(days=30))
        return False
    
    class Meta:
        verbose_name = "Document"
        verbose_name_plural = "Documents"
        ordering = ['type_document', 'nom']
