from django.db import models
from .professionnelDeSante import ProfessionnelDeSante

class Patient(models.Model):
    idPatient = models.AutoField(primary_key=True)
    age = models.IntegerField(6)
    sexe = models.BinaryField()

class Pathologie(models.Model):
    idPathologie = models.AutoField(primary_key=True)
    catPathologie = models.CharField(max_length=60)
    libPathologie = models.CharField(max_length=120)

class Soin(models.Model):
    idSoin = models.AutoField(primary_key=True)
    catSoin = models.CharField(max_length=60)
    libSoin = models.CharField(max_length=120)

class Acte(models.Model):
    idActe = models.AutoField(primary_key=True)
    catActe = models.CharField(max_length=60)
    libActe = models.CharField(max_length=120)
    pathologie = models.ForeignKey(Pathologie, on_delete=models.CASCADE)
    soin = models.ForeignKey(Soin, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    professionnel = models.ForeignKey(ProfessionnelDeSante, on_delete=models.PROTECT, null=True)