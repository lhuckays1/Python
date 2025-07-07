num = [0,0,0,0]
par = []
impar=[]
cont = int(0)
somapar = int(0)
contimpar = int(0)
contpar = int(0)

for cont in range(4):
    num[cont] = int(input(f"Digite o {cont+1}º número: "))
    if(num[cont]%2 == 0):
        somapar = somapar + num[cont]
        contpar += 1


for cont in range(4):
    if(num[cont]%2 == 1):
        impar.append(num[cont])
print(f"O valores impares digitados são:{impar}")

print(f"A soma dos pares é {somapar}")


for cont in range(4):
    if(num[cont]%2 == 0):
        par.append(num[cont])
print(f"O valores impares digitados são:{par}")

