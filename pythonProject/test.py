from math import *
import random


def rand_matrice(ligne,colone):
    resultat_matrix = []
    for col in range(ligne):  # Donne le nombre de ligne en colone
        line_matrix = []
        for line in range(colone):  # Donne le nombre de colone en ligne
            line_matrix.append(random.randint(0,1))
        resultat_matrix.append(line_matrix)  # Donner la valeur final a la matrice
    return resultat_matrix


matrice = rand_matrice(5,6)
print(matrice)