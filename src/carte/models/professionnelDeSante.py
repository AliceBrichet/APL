from django.db import models
from .localisation import Commune
from .infrastructure import Infrastructure


class Profession(models.Model):
    idProfession = models.AutoField(primary_key=True)
    codeProfession = models.IntegerField(null=True)
    libProfession = models.CharField(max_length=120)

class Specialite(models.Model):
    idSpecialite = models.AutoField(primary_key=True)
    codeSpecialite = models.IntegerField(null=True)
    libSpecialite = models.CharField(max_length=120)

class ProfessionnelDeSante(models.Model):
    idProfessionnelDeSante = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=60)
    prenom = models.CharField(max_length=60)
    agePS = models.IntegerField(null=True)
    dateMaj = models.DateField()
    charge = models.IntegerField(null=True)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    specialite = models.ForeignKey(Specialite, on_delete=models.CASCADE, null = True)
    infrastructure = models.ForeignKey(Infrastructure, on_delete=models.PROTECT, null = True)
    commune = models.ForeignKey(Commune, on_delete=models.PROTECT, null = True)