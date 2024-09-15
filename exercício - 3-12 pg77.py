n = int(input("Digite o um número inteiro de 1 a 100: "))
total = n
i = 1
while i <= 5:
    x = float(input("Digite um número com duas casas decimais, exemplo 34.56: "))
    total += x
    i += 1
print("A soma dos valores digitados é {}".format(total))
