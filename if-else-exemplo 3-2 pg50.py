A = int(input("Digite um valor para A: "))
B = int(input("Digite um valor para B: "))

if B==0:
    print("Não é possível calcular a divisão, B igual a zero")
else:
    R = A / B
    print("Resultado: R = %.2f" % R)
