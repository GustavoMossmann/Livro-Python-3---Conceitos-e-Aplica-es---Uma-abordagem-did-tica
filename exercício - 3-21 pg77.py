print("Sequência de Fibonacci\n")

#validação
n = 0
prim = 0
while n < 2 or prim > n:    
    try:
        n = int(input("Digite um nº maior que 2: "))
        prim = int(input("Digite o nº que dará início\
 a sequência: "))
        if n <= 2:
            print("Somente números maiores que 2")
        elif prim > n:
            print("O segundo nº deve ser menor que o\
 primeiro")
    except:
        print("O dado digitado deve ser um\
 número inteiro")

#programa
a = 0
b = 1
print("\n", end="")

i = 0
while i < n:
    c = a + b
    if c > prim:
        print("{}, ".format(c), end="")
    a = b
    b = c
    i += 1

print("\n\nFim da sequência")
