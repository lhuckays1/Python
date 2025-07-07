cont = int(0)
masculino = int(0)

for cont in range (0,3,1):
    nome = str(input(f"Digite o {cont+1}º nome: "))
    sexo = int(input("Escolha o sexo: \n[1] Masculino \n[2] Feminino \n"))

    match sexo:
        case 1:
            masculino +=1

print(f"Foram cadastrados {masculino} homens")
