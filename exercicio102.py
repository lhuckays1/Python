import random
soma = int(0)
cont = int(0)
contar = int(0)

#sorteio = [5, random.randint(1,10), random.randint(1,10), random.randint(1,10)]

sorteio = [0,0,0,0]

for cont in range(4):
    sorteio[cont]= random.randint(0,10)
    
print(sorteio)
num = int(input("Digite um número: "))

for cont in range(4):
    if(num == sorteio[cont]):
        contar = contar + 1
        soma = num + sorteio[cont]

soma = soma + num

print(f"O número {num} apareceu {contar} vezes e a soma é: {soma}")