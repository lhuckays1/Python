num1 = int(input("Digite o 1º número: "))
num2 = int(input("Digite o 2º número: "))
num3 = int(input("Digite o 3º número: "))

soma1 = int(num2 + num3)
soma2 = int(num1 + num3)
soma3 = int(num1 + num2)

if((num1 < soma1) and (num2 < soma2) and (num3 < soma3)):
    print("É um triangulo")
    if((num1 == num2) and (num1 == num3) and (num2 == num3)):
        print("Equilatero")
    
    elif((num1 != num2) and (num1 != num3) and (num2 != num3)):
        print("Escaleno")
    
    elif((num1 == num2) or (num1 == num3) or (num2 == num3) or (num1 != num2) or (num1 != num3) or (num2 != num3)):
        print("Isoceles")

else:
    print("Não é um triangulo")