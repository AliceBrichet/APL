from django.db import models

class Region(models.Model):
    idRegion = models.AutoField(primary_key=True)
    libRegion = models.CharField(max_length=120)

class Departement(models.Model):
    idDepartement = models.AutoField(primary_key=True)
    libDepartement = models.CharField(max_length=120)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

class Commune(models.Model):
    idCommune = models.AutoField(primary_key=True)
    codePostal = models.IntegerField()
    libCommune = models.CharField(max_length=120)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
