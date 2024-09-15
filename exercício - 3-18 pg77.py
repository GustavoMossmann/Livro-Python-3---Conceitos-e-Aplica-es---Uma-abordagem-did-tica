print("\nNúmeros Positivos")
print("\nDigite 0 ou um nº negativo para parar o\
 programa")

#validação dos dados digitados e programa
n = 1
listaN = []
listaNOrdenada = []
i = 0
total = 0

while n > 0:
    try:
        nTxt = input("\nDigite um nº positivo: ")
        n = int(nTxt)
    except:
        print("\n!!!Favor digitar nº inteiro\
 e positivo.")
    else:
        if n <= 0:
            print("Fim do Programa")
            break
            
    listaN.insert(i, n)
    total += n 
    i+= 1

#print(listaN, i)
listaNOrdenada = sorted(listaN)
#print(listaNOrdenada)
i = i - 1
#print(i)
print("\nO maior valor digitado foi: "\
      , listaNOrdenada[i])
print("\nO menor valor digitado foi: "\
      , listaNOrdenada[0])
print("\nA quantidade de valores digitados\
 foi: ", i + 1)
print(f"\nA soma dos valores é igual a: {total:,.2f}")
print(f"\nA média dos valores é igual a:\
 {total/(i+1):,.2f}")


        


