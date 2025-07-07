num = [0,0,0,0]
cont9 = int(0)

for k in range(4):
    num[k] = int(input(f"Digite o {k+1}º valor: "))

    if(num[k] == 9):
        cont9 += 1

print(f"O número 9 apareceu {cont9} vezes")