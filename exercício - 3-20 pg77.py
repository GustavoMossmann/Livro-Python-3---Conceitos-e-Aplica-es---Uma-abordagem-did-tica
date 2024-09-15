print("Somatório de números pares")
# validação
n = 1
while n < 100:
    try:
        nTxt = input("Digite um número inteito,\
 maior ou igual a 100: ")
        n = int(nTxt)
    except:
        print("---Somente números")
    else:
        if n < 100:
             print("---Verifique se o nº digitado\
 é maior ou igual a 100")

#programa
soma = 0
while n != 1:
    pares = n % 2
    if pares == 0:
        soma += n
    n -= 1

print(f"A soma dos números pares é igual a {soma}")
        



    
    
    
