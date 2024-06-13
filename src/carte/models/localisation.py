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
    population2535 = models.IntegerField(null=True)
    population3545 = models.IntegerField(null=True)
    population4555 = models.IntegerField(null=True)
    demandeSoin = models.CharField(max_length=120, default='50')
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
    latitude = models.CharField(max_length=120, null=True)
    longitude = models.CharField(max_length=120, null=True)

class PonDist(models.Model):
    idPonDist = models.AutoField(primary_key=True)
    communeC = models.ForeignKey(Commune, on_delete=models.PROTECT, related_name='commune1')
    communeV = models.ForeignKey(Commune, on_delete=models.PROTECT, related_name='commune2')
    temps = models.CharField(max_length=120)