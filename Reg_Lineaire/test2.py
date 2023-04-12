import pandas as pd
from sklearn.linear_model import LinearRegression

# Chargement des données depuis le fichier Excel
df = pd.read_excel("TP1.xlsx")

# Sélection des colonnes "x1" et "x2" en tant que variables explicatives
# et de la colonne "y" en tant que variable à prédire
X = df[["X1", "X2", "X3" ]]
y = df["Y"]

# Création de l'objet de régression linéaire
reg = LinearRegression()

# Fit du modèle
reg.fit(X, y)

# Calcul des prévisions
y_pred = reg.predict(X)

# Calcul de l'erreur quadratique moyenne
mse = ((y - y_pred) ** 2).mean()

# Calcul du coefficient de détermination R²
r2 = reg.score(X, y)

# Affichage du tableau de l'ANOVA
print("Erreur quadratique moyenne:", mse)
print("Coefficient de détermination R²:", r2)

# Affichage de la matrice d'erreur
print("Matrice d'erreur:")
print(X.cov())
