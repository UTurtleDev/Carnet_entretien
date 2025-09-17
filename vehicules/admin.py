from django.contrib import admin
from .models import Vehicules, Document


class DocumentInline(admin.TabularInline):
    model = Document
    extra = 1
    fields = ['type_document', 'nom', 'fichier', 'date_document', 'date_expiration', 'notes']


@admin.register(Vehicules)
class VehiculesAdmin(admin.ModelAdmin):
    list_display = ['marque', 'modele', 'immatriculation', 'proprietaire', 'annee']
    list_filter = ['carburant', 'transmission', 'proprietaire']
    search_fields = ['marque', 'modele', 'immatriculation']
    inlines = [DocumentInline]


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['vehicule', 'type_document', 'nom', 'date_document', 'date_expiration', 'est_expire']
    list_filter = ['type_document', 'vehicule']
    search_fields = ['nom', 'vehicule__marque', 'vehicule__modele', 'vehicule__immatriculation']
    date_hierarchy = 'date_document'
    
    def est_expire(self, obj):
        return obj.est_expire
    est_expire.boolean = True
    est_expire.short_description = 'Expiré'
