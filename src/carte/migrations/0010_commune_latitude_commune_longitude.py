# Generated by Django 4.2.11 on 2024-06-13 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carte', '0009_remove_professionneldesante_age_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='commune',
            name='latitude',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='commune',
            name='longitude',
            field=models.CharField(max_length=120, null=True),
        ),
    ]