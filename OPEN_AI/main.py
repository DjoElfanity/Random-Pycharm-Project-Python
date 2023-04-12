import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt

# Chargement du fichier Excel
matrice = pd.read_excel('TP1.xlsx')


# Conversion en matrice NumPy
X = matrice.to_numpy()
# Appliquer l'algorithme des K-means
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

# Obtenir les labels prédits pour chaque point de données
labels = kmeans.predict(X)

# Obtenir les centres de chaque cluster
centroids = kmeans.cluster_centers_

# Affichage des données et des centres de chaque cluster
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], marker='*', c='red', s=200)
plt.show()