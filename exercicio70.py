contador = int(1)
soma = int(0)

while (contador != 9999):
    num = int(input("Digite um número: "))
    if(num == 999):
        print("programa finalizado, foi digitado o valor 999")
        break

    soma = soma + num
    contador +=1

print(f"Foram realizadas {contador} tentativas")