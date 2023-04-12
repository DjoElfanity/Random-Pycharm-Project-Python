from math import sqrt
from typing import re
def transpose(matrix):
    resultat_matrix = []
    for col in range (len(matrix[0])): #Donne le nombre de ligne en colone
        line_matrix = []
        for line in range (len(matrix)): #Donne le nombre de colone en ligne
            line_matrix.append(matrix[line][col])
        resultat_matrix.append(line_matrix) #Donner la valeur final a la matrice
    return resultat_matrix
def multiply(matrix1, matrix2):
  m = []
  for i in range(len(matrix1)):
    ligne = []
    for j in range(len(matrix2[0])):
      element = 0
      for k in range(len(matrix1[0])):
        element += matrix1[i][k] * matrix2[k][j]
      ligne.append(element)
    m.append(ligne)
  return m
def multiplication_determinant(matrice , det):
    m = []
    for i in range(len(matrice)):
        ligne = []
        for j in range(len(matrice[0])):
            element = 0
            element += matrice[i][j] * det
            ligne.append(element)
        m.append(ligne)
    return m
def print_matrice(matrix):
    for line in matrix:
        print('  '.join(map(str, line)))
##INVERSION D UNE MATRICE
def Det(A):
    " retourne le déterminat de la matrice A"
    if len(A) == 1:
        return A[0][0]
    if len(A) == 2:
        r = A[0][0] * A[1][1] - A[0][1] * A[1][0]
        return r
    else:
        s = 0
        j = 0
        while j < len(A):
            B = Extrtlincol(j, 0, A)
            if j % 2 == 0:
                s = s + A[j][0] * Det(B)
            else:
                s = s - A[j][0] * Det(B)
            j = j + 1
        return s
def Extrtlincol(m, n, M):
    "retourne la matrice A sans la m ième ligne et la n ième colonne"
    Mlin = len(M)
    result = []
    Rep = []
    for i in range(Mlin):
        if i != m:
            for j in range(Mlin):
                if (j != n):
                    result.append(M[i][j])
    for k in range(0, len(result), Mlin - 1):
        Rep.append(result[k:k + Mlin - 1])
    return Rep
def comat(A):
    "Donne la comatrice d'une matrice A"
    N = len(A)
    k = 0
    com = [None] * N
    while k < N:
        com[k] = [0] * N
        l = 0
        while l < N:
            B = Extrtlincol(k, l, A)
            if (k + l) % 2 == 0:
                com[k][l] = (Det(B))
            else:
                com[k][l] = ((-1) * Det(B))
            l = l + 1
        k = k + 1
    return com
def inversion_matrice(matrice):
    m = multiplication_determinant(transpose(comat(matrice)),1/Det(matrice))
    return m
#regression
def regression(matrice_X , matrice_Y):
    part1 = inversion_matrice((multiply(transpose(matrice_X),matrice_X)))
    part2 = multiply(transpose(matrice_X),matrice_Y)

    resultat = multiply(part1, part2)
    return resultat
def matrice_y_barre(matrice_X, matrice_Y):
    reg = regression(matrice_X,matrice_Y)
    resultat = multiply(matrice_X,reg)
    return resultat
def matrice_erreur(matrice_y_barre, matrice_y):
    m = []
    for i in range(len(matrice_y_barre)):
        ligne = []
         #m= ()
        m.append(matrice_y_barre[i][0] - matrice_y[i][0])
    return m
def correlation(covariance , variance_x , variance_Y):
   resultat = covariance/(sqrt(variance_x)*sqrt(variance_Y))
   return resultat
def moyenne(matrice):
    taille= len(matrice)
    somme =0
    moy=0

    for i in range(len(matrice)):
        #print(matrice[i][0])
        somme += matrice[i][0]
    moy= somme/taille
    return moy
def variance(matrice,moyenne_matrice):
    taille = len(matrice)
    var = 0
    calcul = 0.0
    for i in range(len(matrice)):
        calcul += pow(matrice[i][0]-moyenne_matrice,2)

    var = calcul/taille
    return var
def covariance(matrice_x ,moyenne_x , matrice_y , moyenne_y):
    taille = len(matrice_x)
    somme = 0
    for i in range(len(matrice_x)):
        somme += (matrice_x[i][0]-moyenne_x) * (matrice_y[i][0]-moyenne_y)
    covariance = somme/taille
    return covariance
def SCR(matrice_erreur):
    somme= 0
    for i in range(len(matrice_erreur)):
        somme += matrice_erreur[i]
    return somme
def SCE(matrice_y_barre , moyenne_y):
    somme = 0
    for i in range(len(matrice_y_barre)):
        somme += pow(matrice_y_barre[i][0]-moyenne_y, 2)
    return somme
def SCT(scr , sce):
    somme = scr + sce
    return somme
def tableau_anova(matrice,scr,sce,sct):

    n = (len(matrice))
    p = (len(matrice[0])-1)
    fisher = (sce/p)/(scr/(n-p-1))

    x = [
        [scr,n-p-1,scr/(n-p-1),fisher],
        [sce,p,sce/p,fisher],
        [sct,n-1,sct/(n-1),fisher]
    ]
    return x













