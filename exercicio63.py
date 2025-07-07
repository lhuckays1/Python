contador = int(0)
mult5 = int(0)
mult3 = int(0)

while (contador !=7):
    num = int(input(f"Digite o {contador + 1}º número: "))
    if(num%5 == 0):
        mult5 += 1
    if(num%3 == 0):
        mult3 +=1
    contador +=1

print(f"Foram identificados {mult5} números que são multiplos de cinco e {mult3} números que são multiplos de três")