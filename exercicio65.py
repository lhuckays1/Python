contador = int(1)
media = int(0)
soma = int(0)

while (contador != 9999):
    num = int(input("Digite um número: "))
    resp = str(input("Deseja continuar digitando mais números? "))

    if(num > 0):
        soma = soma + num
        media = soma / contador
        contador +=1

    if(resp == "nao"):
        print(f"A média dos valores positivos é {media}")
        break
    
