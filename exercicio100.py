num = [0,0,0,0]
cont = int(0)
somapar = int(0)
contimpar = int(0)

for cont in range(4):
    num[cont] = int(input(f"Digite o {cont+1}º número: "))
    if(num[cont]%2 == 0):
        somapar = somapar + num[cont]
    else:
        contimpar +=1

print(f"A soma dos pares é {somapar}")
print(f"Foram encontrados {contimpar} números impares")
print(f"Os números impares digitados é: ", end="")
for cont in range(4):
    if(num[cont]%2 == 1):
        if(cont < 3):
            print(f"{num[cont]}", end=", ")
        else:
            print(f"{num[cont]}")