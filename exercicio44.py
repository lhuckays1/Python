hoje = str(input("Digite a data de hoje: "))

if(hoje == "09/09/2022"):
    resposta = str(input("Você sabe o que se comemora nesse dia? "))
    if(resposta == "administrador"):
        resposta = str(input("Você sabe o que vai ter no SENAC hoje? "))
        if(resposta == "sim"):
            print("então você já sabe da surpresa inesperada, nesse caso a surpresa nem é tão inesperada assim")
else:
    print("hoje é dia de uma surpresa INESPERADA")