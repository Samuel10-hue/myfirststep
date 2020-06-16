import random as rnd

prob = rnd.random()

numero = -1
if prob < 0.5:
    numero = 6
else:
    numero = rnd.randint(1, 5)

print(numero)