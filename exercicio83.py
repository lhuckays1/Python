cont = int(0)
erro = int(0)

for cont in range(0,3,1):
    nome = str(input("Digite o nome de usuario: "))
    idade = int(input("Digite a idade: "))

    if(nome == "joao" and idade == 35):
        print("Acesso permitido")
        break
    
    erro += 1

if(cont == 3):
    print("Acesso bloqueado")

print(f"Foi realizado {cont} tentativas")
