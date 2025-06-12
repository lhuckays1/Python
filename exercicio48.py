num1 = int(input("Digite o 1º número: "))
num2 = int(input("Digite o 2º número: "))

maior = int(0)
menor = int(0)

if(num1 == num2):
    print("Os números são igual por isso não existe maior ou menor")
  
if(num1 < num2):
    menor = num1
else:
    menor = num2

if(num1 > num2):
    maior = num1
else:
    maior = num2

print("O menor número é " + str(menor) + " e o maior é " + str(maior))