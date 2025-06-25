from typing import List, Tuple

Objet = Tuple[float, float]  
ListeObjets = List[Objet]

def poids_valeur(tab: ListeObjets, bol: List[bool]) -> Tuple[float, float]:
    poids_total = 0
    valeur_total = 0
    for i in range(len(bol)):
        if bol[i]:
            p, v = tab[i]
            poids_total += p
            valeur_total += v
    return poids_total, valeur_total

def sac_dos(tab: ListeObjets, capacite: float) -> Tuple[List[bool], float]:
    n = len(tab)
    meilleur_choix = []
    meilleure_valeur = 0

    for i in range(2 ** n):
        
        bits = bin(i)[2:].zfill(n)
        choix = [bit == '1' for bit in bits]
        
        poids, valeur = poids_valeur(tab, choix)
        if poids <= capacite and valeur > meilleure_valeur:
            meilleure_valeur = valeur
            meilleur_choix = choix

    return meilleur_choix, meilleure_valeur
objets = [
    (0.3, 180),
    (4.1, 2050),
    (0.6, 280),
    (1.7, 810),
    (2.0, 990),
    (2.9, 1275),
    (5.7, 2570),
    (2.1, 920)
]

capacite_max = 8.0

choix, valeur = sac_dos(objets, capacite_max)
print(valeur)



