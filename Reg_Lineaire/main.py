import pandas as pd

from fonction import *
#sheet = [pd.read_excel("D:\document\TP1.xlsx")]

#Y = [ [200],[300],[350],[450],[500]]
#X =[[12,1],[13,1],[13.25,1],[14,1],[15,1]]

df = pd.read_excel("TP1.xlsx")

# Sélection des colonnes "x1" et "x2" en tant que variables explicatives
# et de la colonne "y" en tant que variable à prédire
X = df[["X1", "X2", "X3" ,"b" ]]
Y = df["Y"]


#Y = [ [120],[130],[150],[190],[230],[290],[340],[400]]
#X =[[1,1],[2,1],[3,1],[4,1],[5,1],[6,1],[7,1],[8,1]]


moyenne_x = moyenne(X)
moyenne_y = moyenne(Y)

variance_x = variance(X,moyenne_x)
variance_y = variance(Y,moyenne_y)
covariance_x_y = covariance(X,moyenne_x, Y,moyenne_y)

print(f"La moyenne de X : {moyenne_x}\nLa moyene de Y = {moyenne_y}")
print("-------------------------")
print(f"La variance de X : {variance_x}\nLa variance de Y = {variance_y}")
print("-------------------------")
print(f"La covariance de X et Y  = {covariance_x_y}")
print("-------------------------")
print(f"La correlation est : {correlation(covariance_x_y,variance_x,variance_y)}")
print("-------------------------")
"""
x = regression(X,Y)
a_chapeau  = x[0]
b_chapeau= x[1]
print(" A chapeau {a_cha}
"""

x = regression(X,Y)
a_chapeau  = x[0]
b_chapeau= x[1]
print(f"A chapeau {a_chapeau} \nB chapeau{b_chapeau}")
print("-------------------------")

print("Matrice Y BARRE: ")
print("-------------------------")
matrice_resultante = matrice_y_barre(X,Y)
print_matrice(matrice_resultante)
print("-------------------------")
print("Matrice Erreur")
print("-------------------------")

matrice_des_erreur = matrice_erreur(matrice_resultante,Y)
#Sommes des carrés
somme_carre_residus =SCR(matrice_des_erreur)
somme_carre_e = SCE(matrice_resultante,moyenne_y)
somme_carre_total = SCT(somme_carre_residus,somme_carre_e)
#-----------------
print(matrice_des_erreur)
print("-------------------------")
print(f"SCR = {somme_carre_residus}")
print(f"SCE = {somme_carre_e}")
print(f"SCT = {somme_carre_total}")
print("-------------------------")
tb_anova = tableau_anova(X,somme_carre_residus,somme_carre_e,somme_carre_total)
print(f"Tableau de l'anova ")
print_matrice(tb_anova)
print(f"\nLe fisher final est {tb_anova[0][3]}")



























