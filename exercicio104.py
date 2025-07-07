import random
cont = int(0)
cor = str("")

saldo = float(input("Digite a quantidade em R$ que deseja depositar: "))

while (saldo !=0):
    aposta = float(input("Digite o valor que deseja apostar: "))
    if(aposta > saldo):
        print(f"O valor apostado é maior que o saldo disponivel em conta \nSaldo disponivel: {saldo}")
    else:
        sorteio = random.randint(1,15)
        if(sorteio >= 9 and sorteio <=15):
            cor = "Vermelho"
        elif(sorteio >= 2 and sorteio <=8):
            cor = "Preto"
        elif(sorteio == 3):
            cor = "Branco"

        #print(f"{sorteio}")
    
        corUser = int(input("Escolha uma cor: \n[1] Vermelho \n[2] Preto \n[3] Branco \n"))
    
        if(corUser == 1 and sorteio >= 9 and sorteio <=15):
            aposta = aposta * 2
            saldo = aposta + saldo
            print(f"A cor selecionada pela blazer é {cor}")
            print(f"Você ganhou! Seu saldo é {saldo:.2f}")
            resp = int(input("Deseja continuar? \n[1] Sim \n[2] Não \n"))
            if(resp == 2):
                print(f"Saldo disponivel: R${saldo:.2f}")
                break
        elif(corUser == 2 and sorteio >= 2 and sorteio <=8):
            aposta = aposta * 2
            saldo = aposta + saldo
            print(f"A cor selecionada pela blazer é {cor}")
            print(f"Você ganhou! Seu saldo é {saldo:.2f}")
            resp = int(input("Deseja continuar? \n[1] Sim \n[2] Não \n"))
            if(resp == 2):
                print(f"Saldo disponivel: R${saldo:.2f}")
                break
        elif(corUser == 3 and sorteio == 3):
            aposta = aposta * 14
            saldo = aposta + saldo
            print(f"A cor selecionada pela blazer é {cor}")
            print(f"Você ganhou! Seu saldo é {saldo:.2f}")
            resp = int(input("Deseja continuar? \n[1] Sim \n[2] Não \n"))
            if(resp == 2):
                print(f"Saldo disponivel: R${saldo:.2f}")
                break
        else:
            saldo = saldo - aposta
            print(f"A cor selecionada pela blazer é {cor}")
            print(f"Você perdeu! Seu saldo é {saldo:.2f}")
            resp = int(input("Deseja continuar? \n[1] Sim \n[2] Não \n"))
            if(resp == 2):
                print(f"Saldo disponivel: R${saldo:.2f}")
                break
            elif(saldo == 0):
                print("Você não possui saldo suficiente")

