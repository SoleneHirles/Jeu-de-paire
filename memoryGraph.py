# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 14:17:59 2019

@author: solene
"""

import tkinter as tk
fen = tk.Tk()
fen.title("Memory")
canvas = tk.Canvas(fen, width=600, height=600, background='cyan')
for i in range (5):
    x=i*120
    y=(i+1)*120
    for j in range (5):      
        rectangle=canvas.create_rectangle(j*120,x,(j+1)*120,y)


#photo = tk.PhotoImage(file="cpp.gif")
#
#
#canvas.create_image(150, 60, image=photo)




#hidden bouton

canvas.pack()#on l'ajoute à la fenetre principale
fen.mainloop() #affiche la fenêtre