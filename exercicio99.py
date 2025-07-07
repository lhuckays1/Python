num = [0,0,0]
cont14 = int(0)

for k in range(3):
    num[k] = int(input(f"Digite o {k+1}º número: "))
    if(num[k] == 14):
        cont14 += 1

print(f"Foram digitados {cont14} vezes o número 14")