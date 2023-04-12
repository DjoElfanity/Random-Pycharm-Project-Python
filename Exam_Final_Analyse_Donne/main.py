import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

print("Programme de  Kmeans")

# Chargement des données à partir d'un fichier CSV
df = pd.read_csv(("iris.csv"), names=['sepal length', 'sepal width', 'petal length',

                                      'petal width', 'target'], usecols=['sepal length', 'sepal width',
                                                                         'target', ])

# Sélection des colonnes à utiliser pour le clustering
X = df[['sepal length', 'sepal width']]

# Entraînement de l'algorithme sur les données
kmeans = KMeans(n_clusters=4).fit(X)

# Ajout de la colonne des labels de cluster au dataframe
df['target'] = kmeans.labels_

# Visualisation des données en utilisant une projection en 2D
plt.scatter(df['sepal length'], df['sepal width'], c=df['target'], cmap='viridis')
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.show()