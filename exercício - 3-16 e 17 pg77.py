print("\nOrdenando os números")

#validação dos dados digitados
n = 0

while n <=0:
    try:
        nTxt = input("\nDigite o nº de\
 valores a serem registrados: ")
        n = int(nTxt)
    except:
        print("\n!!!Favor digitar nº inteiro\
 e positivo.")
    else:
        if n <= 0:
            print("\nDigite um nº positivo e\
 diferentes de zero")

#programa
reais = 0           
i = 0
listaReais = []
valor = 1

while i < n and valor <=n:
    try:
        print("\nValor ",valor)
        reaisTxt = input("Digite o valor: ")
        reais = float(reaisTxt)
    except:
        print("\n!!!Favor digitar um nº real\
 e com 2 casas decimais (ex 34.89)")
    else:
        if reais <= 0:
            print("\nDigite um nº positivo e\
 diferentes de zero")
    
    listaReais.insert(i, reais)
    valor += 1
    i += 1

print("\nOs valores registrados são:\n"\
      , listaReais)

#ordem crescente
listaReaisOrdenada = sorted(listaReais)
listaReaisFormatada = ["{:.2f}".format(num)\
                       for num in listaReaisOrdenada]
print("\nSegue a lista em ordem crescente e\
 formatada:\n", listaReaisFormatada)





















