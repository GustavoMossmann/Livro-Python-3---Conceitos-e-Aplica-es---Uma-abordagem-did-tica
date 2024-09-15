# 3.1. Programa que totaliza um conjunto de valores
# Escreva um programa que leia um número inteiro N e, em seguida, gere N números aleatórios no intervalor [1, 50] e totalize-os. Para gerar números aleatórios, use a função randint, disponível na biblioteca random.

print('\nSoma de números aleatorios\n')
from random import randint
N = int(input("Digite o número de variáveis desejadas entre 1 e 10: "))
total = 0
i = 1
while i <= N:
    x = randint(1,50)
    print("Valor {} gerado = {}".format(i, x))
    total += x
    i += 1
print("A soma dos valores gerados é {}".format(total))

print('\nFim do programa\n')