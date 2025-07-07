cont = int(0)
soma = int(0)

while (cont != 500):
    if(cont%2 == 1):
        if(cont%5 == 0):
            soma = soma + cont
    cont += 1

print(f"A soma de todos os impares multiplos de 5 entre 1 e 500 é {soma}")