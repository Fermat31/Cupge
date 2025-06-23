Case = tuple[int, int]
Position = int
Chemin = dict[Position]

DEPLACEMENTS = [(1, 2), (2, 1), (-1, -2), (-2, -1), (-1, 2), (1, -2), (-2, 1), (2, -1)]

def est_dans_l_echiquier(case: Case, l: int, h: int) -> bool:
    return 0 <= case[0] < h and 0 <= case[1] < l

def numero(case: Case, l: int) -> Position:
    return l * case[0] + case[1]

def coord(position: Position, l: int, h: int = None) -> Case:
    return position // l, position % l

def a_portee_depuis(origine: Position, l: int, h: int) -> list[Position]:
    i, j = coord(origine, l)
    tab = []
    for di, dj in DEPLACEMENTS:
        ni, nj = i + di, j + dj
        if est_dans_l_echiquier((ni, nj), l, h):
            tab.append(numero((ni, nj), l))
    return tab

def existe_ronde(origine: Position, l: int, h: int) -> bool:
    N = l * h

    def existe_rec(position: Position, chemin: Chemin) -> bool:
        if len(chemin) == N:
            return True
        for voisin in a_portee_depuis(position, l, h):
            if voisin not in chemin:
                nouveau_chemin = chemin.copy()
                nouveau_chemin[voisin] = len(chemin)
                if existe_rec(voisin, nouveau_chemin):
                    return True
        return False

    chemin_init = {origine: 0}
    return existe_rec(origine, chemin_init)

def cherche_ronde(origine: Position, l: int, h: int) -> Chemin:
    N = l * h

    def existe_rec(position: Position, chemin: Chemin) -> bool:
        if len(chemin) == N:
            return True
        for voisin in a_portee_depuis(position, l, h):
            if voisin not in chemin:
                nouveau_chemin = chemin.copy()
                nouveau_chemin[voisin] = len(chemin)
                if existe_rec(voisin, nouveau_chemin):
                    chemin.update(nouveau_chemin)
                    return True
        return False

    chemin = {origine: 0}
    if existe_rec(origine, chemin):
        return chemin
    return {}
print(cherche_ronde(0,8,8))

    

