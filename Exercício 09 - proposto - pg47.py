print('\nCálculo da distância entre Coordenadas\n')
from math import sqrt
print('Digite os pontos a seguir:')
x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))

r5 = sqrt((x1 - x2)**2 + (y1 - y2)**2)
print(f'Distância entre esses pontos é: {r5:.3f}')

print('\nFim do programa\n')