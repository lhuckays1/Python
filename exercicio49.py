num1 = int(input("Digite o 1º número: "))
num2 = int(input("Digite o 2º número: "))
num3 = int(input("Digite o 3º número: "))

maior = int(0)
meio = int(0)
menor = int(0)

if((num1 > num2) and (num1 > num3) and (num2 > num3)):
    maior = num1
    meio = num2
    menor = num3

elif((num1 > num2) and (num1 > num3) and (num3 > num2)):
    maior = num1
    meio = num3
    menor = num2

elif((num2 > num1) and (num2 > num3) and (num1 > num3)):
    maior = num2
    menor = num1
    menor = num3

elif((num2 > num1) and (num2 > num3) and (num3 > num1)):
    maior = num2
    meio = num3
    menor = num1

elif((num3 > num1) and (num3 > num2) and (num1 > num2)):
    maior = num3
    meio = num1
    menor = num2

elif((num3 > num1) and (num3 > num2) and (num2 > num1)):
    maior = num3
    meio = num2
    menor = num1

print("O maior número é " + str(maior) + " o do meio é " + str(meio) + " e o menor é " + str(menor))