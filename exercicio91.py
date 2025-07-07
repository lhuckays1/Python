cont = int(0)
soma = int(0)
excedente = int(0)

for cont in range (0,200,1):
    num = int(input(f"Digite o {cont+1}º número: "))
    soma = soma + num
    if(soma > 1000):
        excedente = soma - 1000
        print(f"Excedeu em {excedente}")
        break