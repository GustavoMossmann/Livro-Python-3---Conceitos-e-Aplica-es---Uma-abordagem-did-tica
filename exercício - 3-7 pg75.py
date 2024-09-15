print("É um triângulo?")

m1 = 0
m2 = 0
m3 = 0

while type(m1) == 'str' or type(m2) == 'str' or type(m3) == 'str' or m1 == m2 == m3 == 0:
    try:
        d1 = input("\nDigite a medida 1: ")
        m1 = int(d1)
        d2 = input("\nDigite a medida 2: ")
        m2 = int(d2)
        d3 = input("\nDigite a medida 3: ")
        m3 = int(d3)
    except ValueError:
        print("\nPor favor, digite um número")
    else:
        if m1 == 0 or m2 == 0 or m3 == 0:
            print("\nDigite números diferentes de zero")
        elif (m3 > m1 and m3 > m2 and m1 + m2 > m3) or (m2 > m1 and m2 > m3 and m1 + m3 > m2) or (m1 > m2 and m1 > m3 and m2 + m3 > m1) or m1 == m2 == m3:
            print("\nAS medidas {}, {}, {}, formam um triângulo".format(m1, m2, m3))
            if m1 == m2 == m3:
                print("\nTemos um triângulo do tipo Equilátero")
            elif m1 == m2 or m2 == m3 or m1 == m3:
                print("\nTemos um triângulo do tipo Isósceles")
            else:
                print("\nTemos um triângulo do tipo Escaleno")
        else:
            print("\nAS medidas {}, {}, {}, não formam um triângulo".format(m1, m2, m3))
    finally:
        print("\nObrigado por participar")
            
        
    


            

