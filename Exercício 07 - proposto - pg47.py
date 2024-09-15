# 2.7. Escreva a sequência de comandos para calcular o salário bruto de um pro-fissional que ganha por hora, sabendo que ele ganha R$ 14,25/h e trabalhou 163 horas normais e 20 horas extras (pagam o dobro).

print('\nInício do Programa\n')
print("Salário a receber\n")

valorHora = 14.25
horasTrabalhadas = 163
horasExtras = 20 * 2
salario = ( horasTrabalhadas + horasExtras )* valorHora

print("O salário a receber será de R$: ", salario)

print('\nFim do Programa\n')
