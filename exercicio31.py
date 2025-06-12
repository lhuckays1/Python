s1 = float(input("Digite o salario da 1ª pessoa: "))
s2 = float(input("Digite o salario da 2ª pessoa: "))
s3 = float(input("Digite o salario da 3ª pessoa: "))
s4 = float(input("Digite o salario da 4ª pessoa: "))

maior = float(0)

if(s1 > maior):
    maior = s1

if(s2 > maior):
    maior = s2

if(s3 > maior):
    maior = s3

if(s4 > maior):
    maior = s4

print("O maior salario entre as pessoas é " + str(maior))
