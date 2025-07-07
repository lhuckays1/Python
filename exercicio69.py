contador = int(0)

while (contador != 3):
    num = int(input("Digite um número: "))

    if(num == 20):
        print("Programa finalizado o número digitado é igual a 20")
        break
    
    contador +=1
    if(contador == 3):
        print("programa finalizado, esgotado o número maximo de tentativas")
