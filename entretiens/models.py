from django.db import models
from django.core.exceptions import ValidationError
from vehicules.models import Vehicules

# Create your models here.
def validateur_extentions(value):
    if not value.name.endswith('.pdf'):
        raise ValidationError('Le fichier doit avoir l\'extension .pdf')

class Entretien(models.Model):
    vehicule = models.ForeignKey(Vehicules, on_delete=models.CASCADE, related_name='entretiens')
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
    
    @property
    def kilometrage_separator(self):
        return f"{self.kilometrage:,.0f}".replace(',', ' ')
    
    class Meta:
        ordering = ['-date']


class EntretienPlanifie(models.Model):
    vehicule = models.ForeignKey(Vehicules, on_delete=models.CASCADE, related_name='entretiens_planifies')
    date_prevue = models.CharField(max_length=5, blank=True, null=True, help_text="Format: mm/aa")
    kilometrage_prevu = models.IntegerField(blank=True, null=True)
    type_entretien = models.CharField(max_length=200)
    effectue = models.BooleanField(default=False)
    
    def clean(self):
        if not self.date_prevue and not self.kilometrage_prevu:
            raise ValidationError('Au moins un des champs "Date prévue" ou "Kilométrage prévu" doit être rempli.')
    
    def __str__(self):
        if self.date_prevue and self.kilometrage_prevu:
            return f"{self.vehicule} - {self.type_entretien} ({self.date_prevue} ou {self.kilometrage_prevu:,} km)".replace(',', ' ')
        elif self.date_prevue:
            return f"{self.vehicule} - {self.type_entretien} ({self.date_prevue})"
        elif self.kilometrage_prevu:
            return f"{self.vehicule} - {self.type_entretien} ({self.kilometrage_prevu:,} km)".replace(',', ' ')
        return f"{self.vehicule} - {self.type_entretien}"
    
    @property
    def kilometrage_prevu_separator(self):
        if self.kilometrage_prevu:
            return f"{self.kilometrage_prevu:,.0f}".replace(',', ' ')
        return None
    
    class Meta:
        verbose_name = "Entretien planifié"
        verbose_name_plural = "Entretiens planifiés"
        ordering = ['date_prevue', 'kilometrage_prevu']