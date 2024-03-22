from django.db import models

class Equipement(models.Model):
    idEquipement = models.AutoField(primary_key=True)
    codeEquipement = models.IntegerField()
    libEquiement = models.CharField(max_length=120)

class Infrastructure(models.Model):
    idInfrastructure = models.AutoField(primary_key=True)
    FINESSJ = models.CharField(max_length=150)
    raisonSociale = models.CharField(max_length=120)
    numVoie = models.IntegerField()
    voie = models.CharField(max_length=120)
    telephone = models.IntegerField()
    codeCatIn = models.IntegerField()
    libCatIn = models.CharField(max_length=120)
    longitude = models.CharField(max_length=60)
    latitude = models.CharField(max_length=60)
    dateMaj = models.DateField()
    equipement = models.ForeignKey(Equipement, on_delete=models.CASCADE)