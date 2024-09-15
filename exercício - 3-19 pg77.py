print("Números divisíveis por 2 ou por 3")
print("stop = 0")
n = 1
div2 = [ ]
div3 = [ ]
div2Ordenada = [ ]
div3Ordenada = [ ]
i = 0

#validação e programa
while n!= 0:
    try:
        nTxt = input("Digite um número: ")
        n = int(nTxt)
    except:
        print("!Error! Digite números inteiros\
 diferentes de zero!")
    else:
        nDiv2 = n % 2
        nDiv3 = n % 3
        if nDiv2 == 0 and n != 0:
            div2.insert(i, n)
            div2Ordenada = sorted(div2)
            if nDiv3 == 0:
                div3.insert(i, n)
                div3Ordenada = sorted(div3)
        else:
            if nDiv3 == 0:
                div3.insert(i, n)
                div3Ordenada = sorted(div3)
                      
    print(f"Nº divisíveis por 2:\
 {div2Ordenada}")
    print(f"Nº divisíveis por 3:\
 {div3Ordenada}")
    



        
    
