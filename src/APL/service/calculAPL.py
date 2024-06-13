from carte.models.professionnelDeSante import ProfessionnelDeSante
from carte.models.professionnelDeSante import Profession
from carte.models.localisation import Commune
from carte.models.localisation import PonDist

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


def calculAPL(commune, codes):
    voisins = PonDist.objects.filter(communeC=commune).values_list('commune2', flat=True)
    communes_consideres = voisins + commune

    professionnels = ProfessionnelDeSante.objects.filter(commune=communes_consideres, profession=codeProfession)

    sum_pj_wdij = 0
    for professionnel in professionnels:
        etp = get_etp_from_charge(professionnel.charge)
        
        if professionnel.commune == commune:
            w_dij = 1
        else:
            distance = PonDist.objects.filter(communeC=commune, communeV=professionnel.commune).first()
            if distance:
                w_dij = get_pondist_factor(distance.temps)
            else:
                w_dij = 0
            
        sum_pj_wdij += etp * w_dij

    demande_soins = commune.demandeSoin

    apl = sum_pj_wdij / demande_soins
    
    
    return apl

def createData(option):
    professions = Profession.objects.filter(libProfession=option)
    codeProfession = []
    for profession in professions : 
        codeProfession.append(profession.codeProfession)

    communes = Commune.objects.all()
    data = []
    for c in communes :
        APL = calculAPL(c, codeProfession)
        data[c.libCommune] = [c.latitude, c.longitude, APL]

    return data