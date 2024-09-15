
A = int(input("Digite um número inteiro para A: "))
B = int(input("Digite um número inteiro para B: "))
C = int(input("Digite um número inteiro para C: "))

if A <= B and A <= C:                 #A é o menor número
    if B <= C:                        #encontra o menor entre os restantes
        print("A ordem crescente é: {}, {}, {}".format(A, B, C))
    else:
        print("A ordem crescente é: {}, {}, {}".format(A, C, B))
elif B <= A and B <= C:
    if A <= C:
        print("A ordem crescente é: {}, {}, {}".format(B, A, C))
    else:
        print("A ordem crescente é: {}, {}, {}".format(B, C, A))
else:
    if A <= B:
        print("A ordem crescente é: {}, {}, {}".format(C, A, B))
    else:
        print("A ordem crescente é: {}, {}, {}".format(C, B, A))
    
