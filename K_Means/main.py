from math import  *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot


def calcul_Euclidien(matrice ,centre):
    distance = []
    for i in range(len(matrice)):
        valeur = sqrt(pow(matrice[i][0] - centre[0], 2) + pow(matrice[i][1] - centre[1], 2))
        distance.append(valeur)
    return distance
def calcul_centre(matrice):
    somme_1 = 0
    somme_2 = 0

    for i in range(len(matrice)):
        somme_1 += matrice[i][0]
        somme_2 += matrice[i][1]
    moyenne_1 = somme_1/len(matrice)
    moyenne_2 = somme_2/len(matrice)
    nouveau_centre = [moyenne_1,moyenne_2]

    return nouveau_centre
def create_liste(matrice,distance_c1,distance_c2):
    liste_1.clear()
    liste_2.clear()
    for i in range(len(matrice)):
        if (distance_c1[i] < distance_c2[i]):
            liste_1.append(matrice[i])
        elif (distance_c1[i] > distance_c2[i]):
            liste_2.append(matrice[i])
### ----------------------------DONNEE DE DEPART
matrice_depart = [
    [1,3],
    [3,3],
    [4,3],
    [5,3],
    [1,2],
    [4,2],
    [1,1],
    [2,1]
]
centre_1  =[1,1]
centre_2 = [2,1]
liste_1 = []
liste_2 = []
nouveau_centre_1 = []
nouveau_centre_2 = []
### -------------------------------------------------
### Calcul Distance c1
while(bool!=True):
    distance_c1 = calcul_Euclidien(matrice_depart, centre_1)
    distance_c2 = calcul_Euclidien(matrice_depart, centre_2)

    ###Determiner les listes:
    create_liste(matrice_depart, distance_c1, distance_c2)
    print(liste_1)
    print(liste_2)
    print("-----------------------")
    nouveau_centre_1 = calcul_centre(liste_1)
    nouveau_centre_2 = calcul_centre(liste_2)
    if (nouveau_centre_1 == centre_1 and nouveau_centre_2 == centre_2):
        bool = True
        print("Oui")
        print(f"Centre final 1 : {centre_1}\nCentre final 2: {centre_2}")
        print(f"Liste final 1 : {liste_1}\nListe final 2: {liste_2}")


    else:
        print("ici")
        centre_1 = nouveau_centre_1
        centre_2 = nouveau_centre_2
        print(centre_1)
        print(centre_2)


def x_arrays(liste1,liste2):
    colone_x = []
    for  i in range(len(liste1)):
        colone_x.append(liste1[i][0])
    for i in range(len(liste2)):
        colone_x.append(liste2[i][0])
    return colone_x
def y_arrays(liste1,liste2):
    colone_y = []
    for  i in range(len(liste1)):
        colone_y.append(liste1[i][1])
    for i in range(len(liste2)):
        colone_y.append(liste2[i][1])
    return colone_y

colone_x = x_arrays(liste_1,liste_2)
colone_y = y_arrays(liste_1,liste_2)
plt.scatter(colone_x,colone_y,c='red')
plt.show()


































