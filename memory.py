# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 16:31:11 2019

@author: solen
"""

import numpy as np

def cartesExistent(a,b):
    while(a<0) or (a>jeu.size-1) or (b<0) or (b>jeu.size-1) or (a==b):
        a=int(input("Entrer le numéro de la première carte choisie (entre 1 et 23), Merci"))
        b=int(input("Entrer le numéro de la seconde carte choisie (entre 1 et 23), Merci"))

def carteExiste(carte1, carte2):
    while(carte1<0) or (carte1>jeu.size-1) or (carte1==carte2):
        carte1=int(input("Entrer le numéro de la carte choisie (entre 1 et 23), Merci"))
       
jeu1= np.arange(1,13)
jeu2= np.copy(jeu1)
jeu1,jeu2=np.random.permutation(jeu1),np.random.permutation(jeu2)
jeu=np.concatenate((jeu1,jeu2))

paire=0
while paire!=12:
    a,b=-1,-1
    cartesExistent(a,b)
    while jeu[a]==-10 or jeu[b]==-10:
        if jeu[a]==-10 or jeu[b]==-10:
            a=int(input("paire déjà trouvée, entrer le numéro de d'autres cartes"))
            b=int(input("paire déjà trouvée, entrer le numéro de d'autres cartes"))
            cartesExistent(a,b)
        elif jeu[a]==-10:
            a=int(input("Entrer une carte qui n'a pas encore été trouvé"))
            carteExiste(a,b)
        else:
            b=int(input("Entrer une carte qui n'a pas encore été trouvé"))
            carteExiste(b,a)
    if jeu[a]==jeu[b]:
        paire=paire+1
        print("carte1= ", jeu[a], "et carte2= ", jeu[b])
        print("PAIRE")
        jeu[a],jeu[b]=-10,-10
    else:
        print("carte1= ", jeu[a], "et carte2= ", jeu[b])
