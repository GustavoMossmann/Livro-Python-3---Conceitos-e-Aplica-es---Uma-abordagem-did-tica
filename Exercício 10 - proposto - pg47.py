produto01 = "Boneco Malandrinho"
produto02 = "Spinner Pequeno"
produto03 = "Cubo Mágico"

valorProd01 = float(input("Qual o valor do " + produto01 + ": "))
vendaProd01 = int(input("Quantos " + produto01 + " você vendeu? "))

valorProd02 = float(input("Qual o valor do " + produto02 + ": "))
vendaProd02 = int(input("Quantos " + produto02 + " você vendeu? "))

valorProd03 = float(input("Qual o valor do " + produto03 + ": "))
vendaProd03 = int(input("Quantos " + produto03 + " você vendeu? "))

valorFat = ( valorProd01*vendaProd01 ) + ( valorProd02*vendaProd02 ) + ( valorProd03*vendaProd03 )

print("Você faturou com as vendas de hoje R$: {0:.2f}" .format(valorFat))
