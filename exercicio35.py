num1 = int(input("Digite o 1º número: "))
num2 = int(input("Digite o 2º número: "))
num3 = int(input("Digite o 3º número: "))

somapar = int(0)
somaimpar = int(0)

if(num1%2 == 0):
    somapar = somapar + num1

if(num2%2 == 0):
    somapar = somapar + num2

if(num3%2 == 0):
    somapar = somapar + num3

if(num1%2 == 1):
    somaimpar = somaimpar + num1

if(num2%2 == 1):
    somaimpar = somaimpar + num2

if(num3%2 == 1):
    somaimpar = somaimpar + num3

print("a soma dos números pares é " + str(somapar) + " e a soma dos números impares é " + str(somaimpar))