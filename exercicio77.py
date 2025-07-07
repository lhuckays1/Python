cont = int(0)
contapar = int(0)
contaimpar = int(0)
somapar = int(0)
somaimpar = int(0)
soma = int(0)

for cont in range(0,4,1):
    num = int(input(f"Digite o {cont+1}º número: "))
    if (num%2 == 0):
        print("O número digitado é um número par")
        contapar += 1
        somapar = somapar + num
    
    if(num%2 == 1):
        print("O número digitado é um número impar")
        contaimpar +=1
        somaimpar = somaimpar + num
    soma = somaimpar + somapar
    
print(f"Foram cadastrados {contapar} números pares")
print(f"Foram cadastrados {contaimpar} números impares")
print(f"A soma dos pares é {somapar}")
print(f"A soma dos impares é {somaimpar}")
print(f"A soma geral é {soma}")

