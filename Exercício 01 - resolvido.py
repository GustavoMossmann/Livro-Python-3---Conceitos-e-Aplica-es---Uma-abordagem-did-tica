# 2.1. Escreva um programa que calcule o faturamento de um representante comer-cial que recebe R$ 500,00 fixos e 6% de comissão sobre as vendas do mês. Considere que ele fechou o mês com um valor de R$ 12.398,00 em vendas. Exiba o resultado com duas casas decimais.

print("Início do Programa")
print(" ")
Fixo = 500.00
Vendas = 12398.00
Comissao = 6 / 100

Fat = Fixo + Vendas * Comissao

print("Faturamento do mês = {0:.2f}".format(Fat))
print(" ")

print("Fim do Programa\n\n\n")
