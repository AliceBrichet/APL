from django.db import models
from .localisation import Commune

class Infrastructure(models.Model):
    idInfrastructure = models.AutoField(primary_key=True)
    raisonSociale = models.CharField(max_length=120)
    numVoie = models.IntegerField()
    voie = models.CharField(max_length=120)
    type = models.CharField(max_length=120)
    dateMaj = models.DateField()
    commune = models.ForeignKey(Commune, on_delete=models.PROTECT, null=True)

class Equipement(models.Model):
    idEquipement = models.AutoField(primary_key=True)
    codeEquipement = models.IntegerField()
    libEquiement = models.CharField(max_length=120)
    infrastructure = models.ForeignKey(Infrastructure, on_delete=models.CASCADE, null=True)