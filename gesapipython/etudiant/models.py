from django.db import models

# Create your models here.
class Etudiant(models.Model):
    matricule = models.CharField(max_length=10)
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    #matieres = models.forei