cont = int(0)
contHomem = int(0)

for cont in range(0,3,1):
    nome = str(input("Digite o nome: "))
    sexo = int(input("Escolha o sexo: \n[1] Masculino \n[2] Feminino \n"))

    if(sexo == 1):
        contHomem += 1

print(f"Foram cadastrados {contHomem} homens")