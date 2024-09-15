nome = input("Nome do lutador: ")
peso = float(input("Peso do lutador: "))


if peso < 65:
    print("O lutador {} pesa {} kg e se enquadra na categoria Pena".format(nome, peso))
elif peso >= 65 and peso < 72:
    print("O lutador {} pesa {} kg e se enquadra na categoria Leve".format(nome, peso))
elif peso >= 72 and peso < 79:
    print("O lutador {} pesa {} kg e se enquadra na categoria Ligeiro".format(nome, peso))
elif peso >= 79 and peso < 86:
    print("O lutador {} pesa {} kg e se enquadra na categoria Meio-Médio".format(nome, peso))
elif peso >= 86 and peso < 93:
    print("O lutador {} pesa {} kg e se enquadra na categoria Médio".format(nome, peso))
elif peso >= 93 and peso < 100:
    print("O lutador {} pesa {} kg e se enquadra na categoria Meio-Pesado".format(nome, peso))
else:
    print("O lutador {} pesa {} kg e se enquadra na categoria Pesado".format(nome, peso))
