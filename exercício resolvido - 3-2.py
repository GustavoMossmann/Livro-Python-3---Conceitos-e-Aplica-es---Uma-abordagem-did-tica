print("Sequência de Fibonacci\n")

#validação
n = 0
while n < 2:    
    try:
        n = int(input("Digite um número maior que 2: "))
        if n <= 2:
            print("Somente números maiores que 2")
    except:
        print("O dado digitado deve ser um número inteiro")

#programa
a = 0
b = 1
print("\n0, 1, ", end="")

i = 0
while i < n - 2:
    c = a + b
    print("{}, ".format(c), end="")
    a = b
    b = c
    i += 1

print("\n\nFim da sequência")
