def meme_ligne(n):
    i,j=n//9,n%9
    tab=[]
    for k in range(9):
        if k!=j:
            tab.append(9*i+k)
    return tab

def meme_colonne(n):
    i,j=n//9,n%9
    tab=[]
    for k in range(9):
        if k!=i:
            tab.append(9*k+j)
    return tab

def meme_bloc(n):
    bloc_ligne = (n // 9) // 3
    bloc_col = (n % 9) // 3

    cases = []
    for i in range(3):
        for j in range(3):
            idx = (bloc_ligne * 3 + i) * 9 + (bloc_col * 3 + j)
            if idx != n:
                cases.append(idx)
    return cases
def verifie(n,c,grille):
    tab_ligne=meme_ligne(n)
    tab_colonne=meme_colonne(n)
    tab_bloc=meme_bloc(n)
    for k in tab_ligne:
        i,j=k//9,k%9
        if grille[i][j]==c:
            return False
    for k in tab_colonne:
        i,j=k//9,k%9
        if grille[i][j]==c:
            return False
    for k in tab_bloc:
        i,j=k//9,k%9
        if grille[i][j]==c:
            return False
    return True

def resoud(grille):
    for i in range(9):
        for j in range(9):
            if grille[i][j]==0:
                n=9*i+j
                for c in range(1,10):
                    if verifie(n,c,grille):
                        grille[i][j]=c
                        if resoud(grille):
                            return True
                return False
    return True 