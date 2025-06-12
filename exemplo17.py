num1 = int(input("Digite um valor: "))
num2 = int(input("Digite outro valor: "))
num3 = int(input("Digite outro valor: "))
maior = int(0)

if (num1 > 25):
    maior += 1
if(num2 > 25):
    maior += 1
if(num3 > 25):
    maior += 1

print("Encontramos " + str(maior) + " números maior que 25")