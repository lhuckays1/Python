print("Escolha um humorista: ")
print("[1] Fabio Porchat")
print("[2] Danilo Gentili")
print("[3] Rafinha Bastos")
resp = int(input(""))

cidade = str(input("Digite o nome da sua cidade: "))

match resp:
    case 2:
        if(cidade == "sao paulo"):
            print("Tem show do Danilo Gentili")
    case 3:
        if(cidade == "rio grande do sul"):
            print("Tem Show do Rafinha Bastos")

if(cidade == "araxa"):
    idade = int(input("Digite sua idade: "))
    if(idade > 18):
        print("tem show do Fabio Porchat")
    else:
        print("Não tem show")
