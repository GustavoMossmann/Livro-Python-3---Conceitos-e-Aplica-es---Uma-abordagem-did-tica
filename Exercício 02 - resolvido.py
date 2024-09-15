# 2.1. Escreva um programa que calcule o faturamento de um representante comer-cial que recebe R$ 500,00 fixos e 6% de comissão sobre as vendas do mês. Considere que ele fechou o mês com um valor de R$ 12.398,00 em vendas. Exiba o resultado com duas casas decimais.
# 2.2. Reescreva o programa anterior alterando-o de modo que as vendas do mês sejam lidas do teclado.


print("Início do Programa\n")

Fixo = 500.00
Vendas = float(input("Digite o valor das vendas: "))
Comissao = 6 / 100
Fat = Fixo + Vendas * Comissao

print("Faturamento do mês R$ = {0:.2f}".format(Fat))

print("\nFim do Programa")
