# Generated by Django 4.2.11 on 2024-03-22 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipement',
            fields=[
                ('idEquipement', models.AutoField(primary_key=True, serialize=False)),
                ('codeEquipement', models.IntegerField()),
                ('libEquiement', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Pathologie',
            fields=[
                ('idPathologie', models.AutoField(primary_key=True, serialize=False)),
                ('catPathologie', models.CharField(max_length=60)),
                ('libPathologie', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('idPatient', models.AutoField(primary_key=True, serialize=False)),
                ('age', models.IntegerField(verbose_name=6)),
                ('sexe', models.BinaryField()),
            ],
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('idProfession', models.AutoField(primary_key=True, serialize=False)),
                ('lib', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('idRegion', models.AutoField(primary_key=True, serialize=False)),
                ('libRegion', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Soin',
            fields=[
                ('idSoin', models.AutoField(primary_key=True, serialize=False)),
                ('catSoin', models.CharField(max_length=60)),
                ('libSoin', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Specialite',
            fields=[
                ('idSpecialite', models.AutoField(primary_key=True, serialize=False)),
                ('lib', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='ProfessionnelDeSante',
            fields=[
                ('idProfessionnelDeSante', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=60)),
                ('prenom', models.CharField(max_length=60)),
                ('dateNaiss', models.DateField()),
                ('dateMaj', models.DateField()),
                ('profession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carte.profession')),
                ('specialite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carte.specialite')),
            ],
        ),
        migrations.CreateModel(
            name='Infrastructure',
            fields=[
                ('idInfrastructure', models.AutoField(primary_key=True, serialize=False)),
                ('FINESSJ', models.CharField(max_length=150)),
                ('raisonSociale', models.CharField(max_length=120)),
                ('numVoie', models.IntegerField()),
                ('voie', models.CharField(max_length=120)),
                ('telephone', models.IntegerField()),
                ('codeCatIn', models.IntegerField()),
                ('libCatIn', models.CharField(max_length=120)),
                ('longitude', models.CharField(max_length=60)),
                ('latitude', models.CharField(max_length=60)),
                ('dateMaj', models.DateField()),
                ('equipement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carte.equipement')),
            ],
        ),
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('idDepartement', models.AutoField(primary_key=True, serialize=False)),
                ('libDepartement', models.CharField(max_length=120)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carte.region')),
            ],
        ),
        migrations.CreateModel(
            name='Commune',
            fields=[
                ('idCommune', models.AutoField(primary_key=True, serialize=False)),
                ('codePostal', models.IntegerField()),
                ('libCommune', models.CharField(max_length=120)),
                ('departement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carte.departement')),
            ],
        ),
        migrations.CreateModel(
            name='Acte',
            fields=[
                ('idActe', models.AutoField(primary_key=True, serialize=False)),
                ('catActe', models.CharField(max_length=60)),
                ('libActe', models.CharField(max_length=120)),
                ('pathologie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carte.pathologie')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carte.patient')),
                ('soin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carte.soin')),
            ],
        ),
    ]
