nota = [0,0,0,0,0,0]
cont = int(0)
soma = int(0)
media = int(0)
maior = int(0)
menor = int(99999)

for cont in range(6):
    nota[cont] = int(input(f"Digite a {cont+1}ª nota do aluno: "))

    if (nota[cont] > maior):
        maior = nota[cont]
    if(nota[cont] < menor):
        menor = nota[cont]
    soma = soma + nota[cont]
    media = soma / 6

print(f"A media das notas é: {media}")
for cont in range(6):

    if(nota[cont] > media):
        print(f"Notas que estão acima da média: {nota[cont]}")

print(f"A maior nota é: {maior}")
print(f"A menor nota é: {menor}")

