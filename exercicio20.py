idade = int(input("Digite sua idade: "))
nacionalidade = str(input("Digite sua nacionalidade: "))
sexo = str(input("Informe seu sexo: "))

if(sexo == "masculino" and idade == 18 and nacionalidade == "brasileiro"):
    print("Apto")
else:
    print("Não apto")