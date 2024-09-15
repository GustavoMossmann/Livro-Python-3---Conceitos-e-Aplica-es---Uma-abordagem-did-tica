print("Identificador de números positivos ou negativos")

n = 0

#validação dos dados digitados
while n == 0 or type(n) == 'str':
    try:
        dadoDigitado = input("\nDigite um número, diferente de zero: ")
        n = int(dadoDigitado)
    except:
        print("\n--- {} não é um número, tente novamente".format(dadoDigitado))
    else:
        if n == 0:
            print("\n--- Por favor, digite um número diferente de zero")
        else:
            if n < 0:
               print("\n--- {} é um número negativo".format(n))
            else:
                print("\n--- {} é um número positivo".format(n))
    finally:
        print("\nObrigado por participar!")
            
