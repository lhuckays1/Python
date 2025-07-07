import random
contador = int(0)
soma = int(0)

while (contador != 999):
    sorteio = random.randint(1,9)
    num = int(input("Digite um número: "))
    resp = str(input("Escolha: PAR ou IMPAR: "))
    soma = num + sorteio

    if(soma%2 == 0 and resp == "par"):
        print("USUARIO GANHOU!")
        break
    
    if(soma%2 == 1 and resp == "impar"):
        print("USUARIO GANHOU!")
        break

    contador +=1

print(f"Você teve {contador} derrotas")    



