from multiprocessing import context
from django.shortcuts import HttpResponse, render
from carte.models.professionnelDeSante import ProfessionnelDeSante
from .service.calculAPL import createData

def accueil(request):
    return render(request, "main/accueil.html", )

def carte(request, option):
    contexte = createData(option)
    return render(request, "main/carte.html", contexte)

def stats(request):
    return render(request, "main/stats.html", )

def compte(request):
    return render(request, "main/compte.html", )