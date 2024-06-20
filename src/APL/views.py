from multiprocessing import context
from django.shortcuts import HttpResponse, render
from carte.models.professionnelDeSante import ProfessionnelDeSante
from .service.calculAPL import createData
from .service.calculAPL import getListProfession
from .service.calculAPL import getListAge
from .service.calculAPL import getListSpecialite
import json
from django.http import JsonResponse

def accueil(request):
    return render(request, "main/accueil.html", )

def carte(request, option, age, specialite=None):
    contexte = createData(option, age, specialite)
    listProfession = getListProfession()
    listAge = getListAge()
    listSpecialite = getListSpecialite
    return render(request, "main/carte.html", {'apl': json.dumps(contexte), 'listProfession': listProfession, 'listAge': listAge, 'listSpecialite': listSpecialite})

def stats(request):
    return render(request, "main/stats.html", )

def compte(request):
    return render(request, "main/compte.html", )