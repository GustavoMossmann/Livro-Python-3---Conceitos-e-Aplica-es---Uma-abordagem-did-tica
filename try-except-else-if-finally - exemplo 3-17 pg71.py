print("Número entre 100 e 500")

N = 0
while N < 10 or N > 500:
    try:
        S = input("Digite um número entre 100 e 500: ")
        N = int(S)
    except:
        print("{} não é um número." .format(S))
        N = 0
    else:
        if N < 100 or N > 500:
            print("O valor lido {} está fora do intervalo.".format(N))
        else:
            print("Ok, obrigado por participar!")
    finally:
        print("------")
