print("\nProgressão Geométrica")
print("*Digite números inteiros diferentes de zero")

#validação dos dados
n = 0
r = 0
exp = 0

while n == 0 or r == 0 or exp == 0 or\
      type(n) == 'str' or type(r) == 'str' or\
      type(exp) == 'str':
    try:
         nTxt = input("\nDigite o primeiro termo\
 da PG: ")
         n = int(nTxt)
         rTxt = input("\nDigite a razão da PG: ")
         r = int(rTxt)
         expTxt = input("\nDigite o número de termos\
 da PG: ")
         exp = int(expTxt)
    except ValueError:
        print("\nPor favor, digite somente\
 números inteiros.")
    else:
        if n == 0 or r == 0 or exp == 0:
            print("\nPor favor, digite números\
 diferentes de zero.")

#calculo PG
total = 0
i = 0
print("\nPG = ", end="")
while i < exp:
    PG = n*(r**i)
    print("{}, ".format(PG), end="")
    total += PG
    i += 1
    

print("\n\nA soma dos elementos da PG é\
 igual a: ", total)

            
        
         



        
