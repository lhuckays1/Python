num1 = int(input("Digite o 1º número: "))
num2 = int(input("Digite o 2º número: "))
num3 = int(input("Digite o 3º número: "))

soma1 = int(num2 + num3)
soma2 = int(num1 + num3)
soma3 = int(num1 + num2)

if((num1 < soma1) and (num2 < soma2) and (num3 < soma3)):
    print("É um triangulo")

else:
    print("não é um triangulo")