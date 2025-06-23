def place_cavalier(n, size):
    vec = [(-1, -2), (-2, -1), (-1, 2), (-2, 1),
           (2, -1), (1, -2), (2, 1), (1, 2)]
    tab = []
    i, j = n // size, n % size
    for a, b in vec:
        x, y = a + i, b + j
        if 0 <= x < size and 0 <= y < size:
            tab.append(size * x + y)
    return tab

def solution(n, grille, size, nb):
    x, y = n // size, n % size

    # Marquer la case actuelle avec le numéro de déplacement
    grille[x][y] = nb

    # Si on a atteint la dernière case
    if nb == size * size:
        return True

    # Explorer toutes les cases atteignables
    for i in place_cavalier(n, size):
        xi, yi = i // size, i % size
        if grille[xi][yi] == -1:
            if solution(i, grille, size, nb + 1):
                return True

    # Backtracking : annuler le coup
    grille[x][y] = -1
    return False


grille=[[-1]*8 for _ in range(8)]
print(solution(0,grille,8,1))
print(grille)