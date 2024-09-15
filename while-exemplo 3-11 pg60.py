print("É um número primo?")
print("Digite 0 para sair")
N = int(input("Digite um número: "))

cont = 0
divisor = 2


while divisor < N:
    resto = N % divisor
    if resto == 0:
        cont += 1
    divisor += 1
if cont == 0:
    print("{} é um número primo" .format(N))
else:
    print("{} não é um número primo" .format(N))
        

