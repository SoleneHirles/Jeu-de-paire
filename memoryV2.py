# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 11:57:17 2019

@author: solene
"""

import numpy as np

def carteExiste(carte1, carte2):
    while(carte1<0) or (carte1>jeu.size-1) or (carte1==carte2):
        carte1=int(input("Entrer le numéro de la carte choisie (entre 0 et 23), Merci"))
    return carte1

def carteTrouve(carte):
    while jeu[carte]==-10:
        carte=int(input("paire déjà trouvée, entrer le numéro de d'autres cartes"))
    return carte


jeu1= np.arange(1,13)
jeu=np.concatenate((jeu1,jeu1))
jeu=np.random.permutation(jeu)

paire=0
essai=0
while paire!=12:
    a,b=-1,-1
    a=carteTrouve(carteExiste(a,b))
    print("carte1= ", jeu[a])
    b=carteTrouve(carteExiste(b,a))
    print("carte2= ",jeu[b], "\n")

    if jeu[a]==jeu[b]:
        paire=paire+1
        print("PAIRE \n", paire,"paires trouvées ")      
        jeu[a],jeu[b]=-10,-10
    else:
        print("Essayer à nouveau \n", paire, " paires trouvées" )
    essai=essai+1
    print("---------------------------------------------")
print("FIN DU JEU, vous avez mis ",essai," essais pour trouver ", paire," paires")
    
