contador = int(0)
multa = float(2.00)

while (contador != 99999):
    usuario = str(input("Digite o usuario: "))
    senha = str(input("Digite a senha: "))

    if(usuario == "facil" and senha == "ff"):
        print("Acesso correto")
        break
    else:
        print(f"Você será multado em R${multa} pela sua falha")
        resp = str(input("Deseja tentar novamente? "))
        if(resp == "nao"):
            break
    multa = multa * 2
    contador += 1

