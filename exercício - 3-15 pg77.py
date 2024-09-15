print("\nMultiplos de x")
print("\n*Digite somente numeros inteiros, positivos\
 e diferentes de zero")

#validação dos dados digitados
min = 0
max = 0
min2 = 0
max2 = 0
x = 0

while min <= 0 or min > 10 or max <= 90\
           or max > 100 or x < 2 or x > 9:
    try:
        minTxt = input("\nDigite um número entre\
 01 e 10: ")
        min = int(minTxt)
        maxTxt = input("\nDigite um número entre\
 91 e 100: ")
        max = int(maxTxt)
        xTxt = input("\nDigite o divisor entre\
 02 e 9: ")
        x = int(xTxt)
    except ValueError:
        print("\n---Digite somente números.")
    else:
        if min > max:
            print("\n---Deve ter ocorrido um\
 equívoco na digitação, mas fique tranquilo,\
  já invertemos os valores para você!")
            max2 = min
            min2 = max
            min = min2
            max = max2
        elif min <= 0 or min > 10 or max <= 90\
            or max > 100 or x < 2 or x > 9:
            print("\n---Observe os valores\
  solicitados.")
            

#calculo
minIn = min
multX = 0
total = 0
print("\nEntre os números ", minIn," e ", max,\
      " os múltiplos de ", x," são = ", end="")

while min <= max:
    multX = min % x
    if multX == 0:
        print("{}, ".format(min), end="")
        total += 1
    min += 1

print("\n\nTemos", total,"múltiplos de", x)

    

            
        
         



        
