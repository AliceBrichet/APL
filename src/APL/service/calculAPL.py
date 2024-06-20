from carte.models.professionnelDeSante import ProfessionnelDeSante
from carte.models.professionnelDeSante import Profession
from carte.models.professionnelDeSante import Specialite
from carte.models.localisation import Commune
from carte.models.localisation import PonDist
from django.db.models import Q
import json

pondist_fact = [ 
    (10, 1),
    (15, 2/3),
    (20, 1/3),
    (30, 0),
    (float('inf'), 0)
]

def get_etp_from_charge(charge):
    if charge < 5:
        return 0
    elif 5 <= charge < 15:
        return 0.2
    elif 15<= charge < 20:
        return 0.5
    elif 20 <= charge < 30:
        return 0.7
    else:
        return 1

def get_pondist_factor(temps_trajet):
    for max_time, factor in pondist_fact:
        if temps_trajet <= max_time:
            return factor
    return 0


def calculAPL(commune, codeProfessions, ages, specialite):
    voisins = PonDist.objects.filter(communeC=commune).values_list('communeV', flat=True)
    communes_consideres = list(voisins)
    communes_consideres.append(commune.idCommune)

    bornes = json.loads(ages)

    if specialite :
        specialite = list(Specialite.objects.filter(libSpecialite=specialite))[0].codeSpecialite
        professionnels = list(ProfessionnelDeSante.objects.filter(
            Q(commune__in=communes_consideres) &
            Q(profession__in=codeProfessions) &
            Q(agePS__gte=bornes[0]) & Q(agePS__lte=bornes[1]) &
            Q(specialite=specialite)
        ))
    else : 
        professionnels = list(ProfessionnelDeSante.objects.filter(
            Q(commune__in=communes_consideres) &
            Q(profession__in=codeProfessions) &
            Q(agePS__gte=bornes[0]) & Q(agePS__lte=bornes[1])
        ))

    sum_pj_wdij = 0
    for professionnel in professionnels:
        etp = get_etp_from_charge(professionnel.charge)
        
        if professionnel.commune.idCommune == commune.idCommune:
            w_dij = 1
        else:
            distance = PonDist.objects.filter(communeC=commune, communeV=professionnel.commune).first()
            if distance:
                w_dij = get_pondist_factor(float(distance.temps))
            else:
                w_dij = 0
            
        sum_pj_wdij += etp * w_dij

    demande_soins = float(commune.demandeSoin)

    apl = sum_pj_wdij / demande_soins
    
    
    return apl

def createData(option, bornes, specialite=None):
    professions = Profession.objects.filter(libProfession=option)
    codeProfession = []
    for profession in professions : 
        codeProfession.append(profession.codeProfession)

    communes = Commune.objects.all()
    data = {}
    for c in communes :
        APL = calculAPL(c, codeProfession, bornes, specialite)
        data[c.libCommune] = [c.latitude, c.longitude, APL]

    return data

def getListProfession():
    queryset = Profession.objects.values('libProfession').distinct()
    list = [professions['libProfession'] for professions in queryset]
    return list

def getListAge():
    list = {
        "Tous": [28,65],
        "Entre 28 et 55 ans": [28,55],
        "Entre 55 et 60 ans": [55,65],
        "Plus de 60 ans": [60,65]
    }
    return list

def getListSpecialite():
    queryset = Specialite.objects.values('libSpecialite').distinct()
    list = [specialites['libSpecialite'] for specialites in queryset]
    return list