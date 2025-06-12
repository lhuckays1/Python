num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite outro número: "))

contapar = int(0)
contaimpar = int(0)


if(num1%2 == 0):
   contapar += 1
else:
   contaimpar += 1

if(num2%2 == 0):
   contapar += 1
else:
   contaimpar += 1

if(num3%2 == 0):
   contapar += 1
else:
   contaimpar += 1

print("Foram encontrados " + str(contapar) + " números pares e " + str(contaimpar) + " números impares")

