cont = int(0)
contapar = int(0)
somapar = int(0)

for cont in range(0,6,1):
    num = int(input(f"Digite o {cont+1}º número: "))
    if(num%2 == 0):
        somapar = somapar + num
        contapar +=1

print(f"Foram digitados {contapar} números pares e a soma desses números pares é {somapar}")