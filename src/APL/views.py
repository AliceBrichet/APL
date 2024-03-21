from multiprocessing import context
from django.shortcuts import HttpResponse, render

def accueil(request):
    return render(request, "main/accueil.html", )

def carte(request):
    return render(request, "main/carte.html", )

def stats(request):
    return render(request, "main/stats.html", )

def compte(request):
    return render(request, "main/compte.html", )