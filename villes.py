# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 12:29:53 2021

@author: camil
"""

from tkinter import *

xMin = 0
xMax = 0
yMin = 0
yMax = 0

textCity = ""
choice = ''


def chooseMap(event):# Affiche la taille de carte sélectionnée
    global xMin, xMax, yMin, yMax, choice
    readFile()
    map = ['494x516','742x773','989x1031']
    f = listMap.curselection() # Récupère la place de l'élément sélectionné dans la liste
    str(f)
    try:
        place = f[0]
        nameImage = map[place] # Sélectionne le nom de la carte choisie
        can.delete(ALL) # Supprime la carte précédente du canva
    except IndexError:
        nameImage = choice
    print("nameImage = ", nameImage)
    if nameImage == '494x516':
        xMin = 262 # Sélectionne les coordonnées des points de repères
        xMax = 121
        yMin = 37
        yMax = 386
        imageMap = PhotoImage(file = 'map_france_494x516.gif')
        PhotoMap = can.create_image(0,0,anchor = 'nw',image = imageMap) 
        mapCircle() # Dessine les cercles
    if nameImage == '742x773':
        xMin = 393
        xMax = 180
        yMin = 54
        yMax = 581
        imageMap = PhotoImage(file = 'map_france_742x773.gif')
        PhotoMap = can.create_image(0,0,anchor = 'nw',image = imageMap)
        mapCircle()
    if nameImage == '989x1031':
        xMin = 524
        xMax = 242
        yMin = 73
        yMax = 774
        imageMap = PhotoImage(file = 'map_france_989x1031.gif')
        PhotoMap = can.create_image(0,0,anchor = 'nw',image = imageMap)
        mapCircle() # Place les cercles sur la carte
    choice = nameImage
    print("nameImage =", nameImage)
    fen.mainloop()

def mapFonction(variable1, min1, min2, max1, max2):# Convertit les échelles
    variable2 = min2 + (max2-min2) * ((variable1-min1) / (max1-min1)) # Calcul pour passer d'une échelle à une autre
    return variable2

def readFile(): # Lit le fichier
    global lat, long, cities
    lat = []
    long = []
    cities = []
    file = open('villes.txt', 'r') # Lit le fichier
    k = 0
    for j in file : # Stocke les valeurs du fichier dans 3 listes
        line = j
        cities.insert(k,line[0:30])
        lat.insert(k,line[30:36])
        long.insert(k,line[56:63])
        k = 1 + k

def mapCircle():# Place et dessine les cercles sur la carte
    for a in range (0,113): # Pour toutes les valeurs de la liste 
        variable1 = float(long[a])
        longitude = mapFonction(variable1,2.58,xMin,-1.8,xMax) # Conversion d'une échelle à une autre
        long[a] = longitude # Stocke la nouvelle valeur dans la liste
    for b in range (0,113):
        variable1 = float(lat[b])
        latitude = mapFonction(variable1,51.25,yMin,43.31,yMax)
        lat[b] = latitude # Stocke la nouvelle valeur dans la liste
    for c in range (0,113) :
        y = lat[c]
        x = long[c]
        can.create_oval(x-2,y-2,x+2,y+2, width = 1,outline = 'black') # Créer un cercle sur la carte à l'emplacement de chaque ville

def cityCircled(event):# Entoure la ville sélectionnée
    can.delete("oval") # Supprime l'ancien cercle
    citySelected = listCities.curselection() # Stocke la place de l'élément sélectionné dans la liste de villes
    str(citySelected)
    print("tuple :",citySelected)
    placeCity = citySelected[0]
    print("placeCity =",placeCity)
    xCity = float(long[placeCity]) # Stocke la longitude correspondante
    yCity = float(lat[placeCity]) # Stocke la latitude correspondante
    print("y = ", yCity)
    print("x= ", xCity)
    oval = can.create_oval(xCity-3,yCity-3,xCity+3,yCity+3, width = 2,outline = 'red', tags="oval")
    fen.mainloop()
    
    
def clic(event):# Nomme la ville sur laquelle on clique 
    global text1
    xClic = event.x # Stocke la position du clic sur le canva
    yClic = event.y
    for m in range(0,113): # Teste à quelle coordonnées correspondent celles stockées
        xTest = int(long[m])
        yTest = int(lat[m])
        if (xClic-20 < xTest < xClic+20) and (yClic-20 < yTest < yClic+20):  # Si les coordonnées correspondent avec une marge de 20 pixels
            xClic = xTest
            yClic = yTest
            n = m # Stocke la place de la ville dans la liste
            break
    if (xClic != event.x) and (yClic != event.y) : 
        textCity = "Cette ville est " + str(cities[n]) # Affiche le nom de la ville sur laquelle on a cliqué
    else:
        textCity = "Pas de ville ici, soyez plus précis."
    text1 = Label(fen, height = 1, width = 30, text = textCity)
    text1.place(x = 1040, y = 510)
    fen.mainloop()
    
    
    
    
    
    
readFile() # Remplir les listes avec les données du fichier
fen = Tk() # Créer une fenêtre

listCities = Listbox(fen) # Créer la liste des villes
listCities.pack(side = RIGHT, padx = 5, pady = 5)
for k in range (0,len(cities)):  # Insert tous les noms de ville dans la liste
    nameCity = str(cities[k])
    listCities.insert(END,nameCity)

listMap = Listbox(fen) # Créer la liste des cartes
listMap.pack(side = RIGHT, padx = 5, pady = 5)
listMap.insert(END,"494x516") # Insert les options de la liste
listMap.insert(END,"742x773")
listMap.insert(END,"989x1031")
    
leave = Button(fen,text = 'Quitter', command = fen.destroy) # Créer le bouton quitter
leave.place(x = 1020, y = 600)    
    
can = Canvas(fen, width = 989, height = 1031, bg = 'ivory') # Créer le caneva 
can.pack()   
oval = can.create_oval(1000,1000,1001,1001, width = 1, tags="oval") # Créé un rond en dehors du caneva pour entourer en rouge les villes

text0 = Label(fen, height = 1, width = 40, text ='Cliquez sur une ville pour connaître son nom.')
text0.place(x = 991, y = 480)

text1 = Label(fen, height = 1, width = 90, text = textCity)
text1.place(x = 1000, y = 510)

text2 = Label(fen, height = 1, width =15, text = 'Choissisez une carte.')
text2.place(x = 1003, y = 250)

text3 = Label(fen, height = 1, width =15, text = 'Localisez une ville.')
text3.place(x = 1136, y = 250)

can.bind('<Button-1>', clic)
listMap.bind("<<ListboxSelect>>",chooseMap)
listCities.bind("<<ListboxSelect>>",cityCircled) 

fen.mainloop()