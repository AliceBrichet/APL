from django.db import models


class Profession(models.Model):
    idProfession = models.AutoField(primary_key=True)
    lib = models.CharField(max_length=120)

class Specialite(models.Model):
    idSpecialite = models.AutoField(primary_key=True)
    lib = models.CharField(max_length=120)

class ProfessionnelDeSante(models.Model):
    idProfessionnelDeSante = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=60)
    prenom = models.CharField(max_length=60)
    dateNaiss = models.DateField()
    dateMaj = models.DateField()
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    specialite = models.ForeignKey(Specialite, on_delete=models.CASCADE)