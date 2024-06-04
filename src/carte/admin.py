from django.contrib import admin
from .models.acte import Patient

# Register your models here.

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    pass