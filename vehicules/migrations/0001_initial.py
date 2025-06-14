# Generated by Django 5.2.3 on 2025-06-15 09:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proprietaires', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marque', models.CharField(max_length=50)),
                ('modele', models.CharField(max_length=50)),
                ('annee', models.DateField()),
                ('annee_achat', models.DateField()),
                ('kilometrage_achat', models.IntegerField()),
                ('couleur', models.CharField(max_length=50)),
                ('immatriculation', models.CharField(max_length=9)),
                ('chevaux_fiscaux', models.IntegerField()),
                ('chevaux_din', models.IntegerField()),
                ('carburant', models.CharField(blank=True, choices=[('Diesel', 'Diesel'), ('Essence', 'Essence'), ('Electrique', 'Electrique'), ('Hybride', 'Hybride')], max_length=50, null=True)),
                ('transmission', models.CharField(blank=True, choices=[('Manuelle', 'Manuelle'), ('Automatique', 'Automatique')], max_length=50, null=True)),
                ('photo', models.ImageField(upload_to='')),
                ('proprietaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proprietaires.proprietaire')),
            ],
        ),
    ]
