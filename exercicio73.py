cont = int(0)
nome = str("")
telefone = str("")

for cont in range(0,5,1):
    nome = str(input("Digite o nome: "))
    telefone = str(input("Digite o telefone: "))

    print(f"O nome cadastrado foi {nome} e o telefone foi {telefone}")