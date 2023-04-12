import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Chargement des données depuis le fichier CSV
df = pd.read_csv("iris.csv")

# Sélection des colonnes à utiliser pour l'ACP
data = df.select_dtypes(include=[int, float])

# Création de l'objet ACP
pca = PCA(n_components=2)

# Fit et transformation des données
X_pca = pca.fit_transform(data)

# Affichage du plot
plt.scatter(X_pca[:, 0], X_pca[:, 1])
plt.show()
