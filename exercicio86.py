import random
sorteio = random.randint(1,10)
cont = int(0)
maior = int(0)
menor = int(0)

while True:
    num = int(input("Digite um número: "))
    if(num > sorteio):
        print("Você errou! Tente chutar um número menor")
    elif(num < sorteio):
        print("Voce errou! Tente chutar um número maior")
    elif(num == sorteio):
        print(f"Sucesso você acertou após {cont} tentativas")
        break
    cont += 1

