idade = int(input("Digite a idade: "))

if(idade == 18):
    sexo = str(input("Digite o sexo: "))
    if(sexo == "masculino"):
        nacionalidade = str(input("Digite a nacionalidade: "))
        if(nacionalidade == "brasileiro"):
            print("Bem vindo Soldado")
        else:
            print("Dispensado")
    else:
        print("Dispensado")
else:
    print("Dispensado")