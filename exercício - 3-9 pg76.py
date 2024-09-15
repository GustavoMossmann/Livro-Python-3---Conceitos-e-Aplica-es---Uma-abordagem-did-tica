print("Pagamento por Horas Trabalhadas")
valorHora = 0
horasTrabalhadas = 0
horasExtras = 0

while valorHora == 0 or horasTrabalhadas == 0 or horasExtras == 0 or numValorHora == 0 or \
      (numHorasTrabalhadas == 0 and numHorasExtras == 0) or type(valorHora) == 'str' or \
      type(horasTrabalhadas) == 'str' or type(horasExtras) == 'str':
    try:
        valorHora = input("\nDigite o valor pago por hora em R$: ")
        numValorHora = float(valorHora)
        horasTrabalhadas = input("\nDigite o número de horas trabalhadas: ")
        numHorasTrabalhadas = int(horasTrabalhadas)
        horasExtras = input("\nDigite o número de horas extras trabalhadas: ")
        numHorasExtras = int(horasExtras)
    except:
        print("\n!!!Error!!! Por favor, verifique os valores, R$ 00.00 e número inteiro para horas")
    else:
        if numValorHora == 0:
            print("\n!!!Error!!! Valor da hora deve ser diferente de zero")
        
        elif numHorasTrabalhadas == 0 and numHorasExtras == 0:
            print("\n!!!Error!!! Algum dos campos, horas trabalhadas ou horas extras, deve ser preenchido")
        else:
            pagamento = (numValorHora * numHorasTrabalhadas) + (numValorHora * numHorasExtras * 2)
            print("\nO valor a ser recebido pelo profissional é de R$ {0:.2f}".format(pagamento))
        
    
        
