print("\nSeparando e somando números positivos e negativos")
print("\nPara finalizar digite 0")

n = int(input("\nDigite um número inteiro positivo ou negativo: "))
negativos = 0
positivos = 0

while n != 0:
    if n < 0:
        negativos -= n
    else:
        positivos += n
    n = int(input("\nDigite um número inteiro positivo ou negativo: "))

print("\nA soma dos positivos é igual a: {}\
 e a soma dos negativos é igual a: -{}".format(positivos, negativos))
print("\nObrigado por participar!")

        
