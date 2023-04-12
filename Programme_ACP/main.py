import numpy as np
matrice = np.array([
   [3.,6.],
   [4.,7.],
    [5.,9.],
    [8.,10.]
]
)
A = matrice

meanPoint = matrice.mean(axis = 0)

# subtract mean point
matrice -= meanPoint
print("matrice centree")
print(matrice)

print('------------------')
ecart_type = np.std(matrice)
reduite = np.divide(matrice, ecart_type)
print("la matrice reduite")
print(reduite)

print('----------------------')
trans = np.transpose(reduite)
mul = np.dot(trans, reduite)
corr = np.divide(mul, 4)
print("la matrice de correlation")
print(corr)

print("----------------------")
diago = np.diag(corr)
print("la matrice diagonale")
print(diago)
print(f"Valeur Propre 1 = {diago[0]}\nValeur Propre 2 = {diago[1]}")
print(f"Variance 1 = {diago[0]/2}\nVariance 2 = {diago[1]/2}")

print("----------------------")
cumul = diago[0]/2 + diago[1]/2
print(f"Le cumul est : {cumul} ")



