import random as rnd
import matplotlib.pyplot as plt

x_atual = 0
y_atual = 0

for i in range(1, 51):
    x_anterior = x_atual
    y_anterior = y_atual
    
    direcao = rnd.randint(1, 4)
    distancia = rnd.randint(1, 5)
    if direcao == 1:
        y_atual = y_atual + distancia
    elif direcao == 2:
        x_atual = x_atual + distancia
    elif direcao == 3:
        y_atual = y_atual - distancia
    else:
        x_atual = x_atual - distancia
    
    plt.plot([x_anterior, x_atual], [y_anterior, y_atual], "-bo")        

plt.show()
