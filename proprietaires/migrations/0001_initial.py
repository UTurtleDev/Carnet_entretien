# Generated by Django 5.2.3 on 2025-06-15 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proprietaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('adresse', models.CharField(max_length=50)),
                ('code_postal', models.CharField(max_length=5)),
                ('ville', models.CharField(max_length=50)),
                ('telephone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
