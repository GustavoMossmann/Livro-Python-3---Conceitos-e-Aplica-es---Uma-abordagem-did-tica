# 2.1. Faça X = 0.0 e Y = 18. Verifique o tipo de dado que o Python atribuiu a cada um. Faça Z = X + Y e verifique o resultado calculado e armazenado em Z. Verifique com qual tipo de dado foi criado o objeto Z.

print('Início do Programa\n\n')

x = 0.0
y = 18
print("x é do tipo: ", type(x))
print("y é do tipo: ", type(y))

z = x + y
print('z = x + y')
print(f"z é igual a: {z}")
print(f"z é do tipo: {type(z)}")

print('\n\nFim do Programa')