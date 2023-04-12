import pandas as pd
from fonction import *
import numpy as np
import matplotlib.pyplot as plt
import math

#sheet = pd.read_excel("D:\document\TP1.xlsx")

def Stand(matrice):
    uno = np.ones((1,len(matrice)))
    p1 = matrice - np.dot(np.dot(np.transpose(uno),uno),matrice)/len(matrice)
    return p1
def covMat(mat):
    return np.dot(np.transpose(mat),mat)/len(mat)

matrice_base =[
[3,6],
[4,7],
[5,9],
[8,10]
]

matrice = Stand(matrice_base)
matrice_cov = covMat(matrice)

def quiz(matrice, cov):
    new_matrice = matrice
    for i in range(len(matrice)):
        new_matrice[i][0]= matrice[i][0]/sqrt(cov[0][0])
        new_matrice[i][1]= matrice[i][1]/sqrt(cov[1][1])
    return new_matrice
z = quiz(matrice,matrice_cov)
print_matrice(z)




