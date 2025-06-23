def generateur_U(a):
	u0=a
	yield u0
	while True:
		yield (u0+a/u0)/2
		u0=(u0+a/u0)/2
gen=generateur_U(2)
print(next(gen))
print(next(gen))
print(next(gen))
def precision_U(a,epsilon):
    gen=generateur_U(a)
    b=a
    n=0
    while abs(b-a**1/2) > epsilon :
        c=next(gen)
        b=c
        n=n+1
    return n,b
print(precision_U(2,10**-7))







####################################################################################
#coding:utf8
import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

class GrapheOriente:
    def __init__(self,liste_sommets,inverse):
        self.nombre_sommets = len(liste_sommets)
        self.arcs = { sommet:[] for sommet in liste_sommets}
        self.liste_sommets = liste_sommets
        self.nombre_arcs = 0
        self.rouges=[]
        self.verts=[]
        self.blanc=[]
        self.inverse=inverse
              
    def get_voisinage_out(self,sommet_depart):       
        return self.arcs[sommet_depart]
    
    def get_voisinage_in(self,sommet_arrivee):      
        return [self.arcs[sommet_depart] for sommet_depart in self.arcs if self.arcs[sommet_depart] == sommet_arrivee]
    
    def get_voisinage_out_str(self,sommet_depart):
        return " ".join([str(sommet_arrivee) for sommet_arrivee in self.get_voisinage_out(sommet_depart)])
    
    def __str__(self):
        return "\n".join([str(sommet_depart)+" : "+self.get_voisinage_out_str(sommet_depart) for sommet_depart in self.arcs])+'\n'
             
    def set_arc(self,sommet_depart, sommet_arrivee):
        self.arcs[sommet_depart].append(sommet_arrivee)
        self.nombre_arcs += 1

    def get_arcs(self):
        return [ (sommet_depart, sommet_arrivee) for sommet_depart in self.arcs for sommet_arrivee in self.arcs[sommet_depart]]
  
    def set_noyau(self):
        if self.inverse==0:
            for sommet in self.liste_sommets:
                if len(self.arcs[sommet])==0:
                    self.rouges.append(sommet)
                else:
                    self.blanc.append(sommet)
            while len(self.blanc)!=0:
                for sommet in self.blanc[:]:
                    for t in self.rouges:
                        if t in self.arcs[sommet]:
                            self.verts.append(sommet)
                            self.blanc.remove(sommet)
                            break
                for sommet in self.blanc[:]:
                    if all(t in self.verts for t in self.arcs[sommet]):
                        self.rouges.append(sommet)
                        self.blanc.remove(sommet)

                        for p in self.liste_sommets:
                            if sommet in self.arcs[p] and p in self.blanc:
                                self.verts.append(p)
                                self.blanc.remove(p)
        elif self.inverse==1:
            for sommet in self.liste_sommets:
                if len(self.arcs[sommet])==0:
                    self.verts.append(sommet)
                else:
                    self.blanc.append(sommet)
            while len(self.blanc)!=0:
                for sommet in self.blanc[:]:
                    for t in self.rouges:
                        if t in self.arcs[sommet]:
                            self.verts.append(sommet)
                            self.blanc.remove(sommet)
                            break
                for sommet in self.blanc[:]:
                    if all(t in self.verts for t in self.arcs[sommet]):
                        self.rouges.append(sommet)
                        self.blanc.remove(sommet)

                        for p in self.liste_sommets:
                            if sommet in self.arcs[p] and p in self.blanc:
                                self.verts.append(p)
                                self.blanc.remove(p)
    

            

                
 
    def jeu_noyau(self,sommet):
        self.joueur = 1
        liste_coups = self.get_voisinage_out(sommet)
        while len(liste_coups)!=0:#le joueur peut jouer
            if sommet in self.verts:
                l=[s for s in liste_coups if s not in self.verts]
                sommet=random.choice(l)
            else:
                sommet=random.choice(liste_coups)
            self.joueur = 2 if self.joueur == 1 else 1  
            liste_coups = self.get_voisinage_out(sommet) 
            
        if self.joueur == 1:
           print("Le joueur 2 a gagné")
        else:
           print("Le joueur 1 a gagné")
    
    def affiche_graphe(self):
        Gn = nx.DiGraph()
        Gn.add_nodes_from(self.liste_sommets)
        self.rouges = self.liste_sommets#ligne à retirer lorsque set_noyau sera implémenté
        Gn.add_edges_from([ (sommet_depart,sommet_arrivee) for sommet_depart in self.liste_sommets for sommet_arrivee in self.arcs[sommet_depart]])        
        couleurs = ["red" if sommet in self.rouges else "green" for sommet in self.liste_sommets]
        nx.draw_circular(Gn, node_color =couleurs,with_labels=True)
        plt.show()



class rectangle(GrapheOriente):
    def __init__(self,nombre_lignes,nombre_colonnes):
        self.nombre_lignes=nombre_lignes
        self.nombre_colonnes=nombre_colonnes
        self.liste_sommets=[(a,b) for a in range(self.nombre_lignes+1) for b in range(self.nombre_colonnes+1) if a!=b]
        self.liste_sommets.append((0,0))
        self.nombre_sommets=len(self.liste_sommets)
        self.arcs={somme:[] for somme in self.liste_sommets}
        self.nombre_arcs=0
    def set_arcs(self):
        for a,b in self.liste_sommets:
            for c,d in self.liste_sommets:
                if a==c+1 and b==d:
                    self.set_arc((a,b),(c,d))
                elif a==c and b==d+1:
                    self.set_arc((a,b),(c,d))


if __name__ == "__main__":
  G = GrapheOriente(list(range(50)))
  print(G)
  G.affiche_graphe()
  D1=rectangle(15,15)
  D1.set_arcs()
  print(D1)
  D1.affiche_graphe()
  #############
  D2=rectangle(15,14)
  D2.set_arcs()
  print(D2)
  D2.affiche_graphe()
  ###########
  D3=rectangle(15,13)
  D3.set_arcs()
  print(D3)
  D3.affiche_graphe()
  #########
  D4=rectangle(15,12)
  D4.set_arcs()
  print(D4)
  D4.affiche_graphe()