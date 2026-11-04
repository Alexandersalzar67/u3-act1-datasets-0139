import pandas as pd
import os
# Alexander Salazar nc = 0139
# URL del dataset público para leer datos de iris.csv
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
# Descargar y cargar el CSV
datos = pd.read_csv(url)

print(datos)
# Guardar una copia local en la carpeta datasets
datos.to_csv("datasets/iris.csv", index=False)
# Explorar los datos
print("PRIMERAS 5 FILAS")
print(datos.head())
print()
print("\\nCANTIDAD DE FILAS Y COLUMNAS")
print(datos.shape)
print("\\nNOMBRES DE LAS COLUMNAS")
print(datos.columns.tolist())
print("\\nINFORMACION DEL DATASET")
print(datos.info())
print("\\nCARACTERISTICAS (X)")
X = datos.drop(columns=["species"])
print(X.head())
print("\\nVARIABLE OBJETIVO (y)")
y = datos["species"]
print(y.head())
print("\\nESPECIES REGISTRADAS")
print(y.unique())