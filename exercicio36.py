n1 = int(input("Digite o 1º número: "))
n2 = int(input("Digite o 2º número: "))
n3 = int(input("Digite o 3º número: "))
n4 = int(input("Digite o 4º número: "))

contapar = int(0)
somapar = int(0)
maior = int(0)

if(n1%2 == 0):
    contapar += 1
    somapar = somapar + n1

if(n2%2 == 0):
    contapar += 1
    somapar = somapar + n2

if(n3%2 == 0):
    contapar += 1
    somapar = somapar + n3

if(n4%2 == 0):
    contapar += 1
    somapar = somapar + n4

if(n1 > maior):
    maior = n1

if(n2 > maior):
    maior = n2

if(n3 > maior):
    maior = n3

if(n4 > maior):
    maior = n4

print("Foram digitados " + str(contapar)+ " números pares")
print("A soma desses números pares é " + str(somapar))
print("O maio número par é " + str(maior))