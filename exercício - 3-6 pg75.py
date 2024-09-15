print("Comparador de Dois Números")

n1 = 0
n2 = 0

#validação dos dados digitados
while n1 == n2 or type(n1) == 'str' or type(n2) == 'str' or n1 == 0 or n2 == 0:
    try:
        dadoDigitado1 = input("\nDigite um número, diferente de zero: ")
        n1 = int(dadoDigitado1)
        dadoDigitado2 = input("\nDigite um número, diferente de zero: ")
        n2 = int(dadoDigitado2)
    except ValueError:
        print("\n--- Por favor, digite somente nímeros")
    else:
        if n1 == 0 or n2 == 0 or n1 == n2:
            print("\n--- Por favor, digite um números não semelhantes e diferente de zero")
        else:
            if n1 > n2:
               print("\n--- {} é maior que {}".format(n1, n2))
            else:
                print("\n--- {} é maior que {}".format(n2, n1))
    finally:
        print("\nObrigado por participar!")



            
