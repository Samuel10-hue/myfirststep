import pandas as pd
from numpy import corrcoef

dados = pd.read_csv("mtcars.csv")

lista_gear = list(dados["gear"])
lista_cyl = list(dados["cyl"])
lista_hp = list(dados["hp"])

corr_diretor = corrcoef(lista_gear, lista_hp)[0][1]
corr_estagiario = corrcoef(lista_cyl, lista_hp)[0][1]

print(corr_diretor)
print(corr_estagiario)