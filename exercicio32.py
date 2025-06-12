idade1 = int(input("Digite a idade da 1ª pessoa: "))
idade2 = int(input("Digite a idade da 2ª pessoa: "))
idade3 = int(input("Digite a idade da 3ª pessoa: "))
idade4 = int(input("Digite a idade da 4ª pessoa: "))

maior = int(0)
menor = int(99999)

if(idade1 > maior):
    maior = idade1

if(idade2 > maior):
    maior = idade2

if(idade3 > maior):
    maior = idade3

if(idade4 > maior):
    maior = idade4

if(idade1 < menor):
    menor = idade1

if(idade2 < menor):
    menor = idade2

if(idade3 < menor):
    menor = idade3

if(idade4 < menor):
    menor = idade4

print("O mais jovem tem " + str(menor) + " anos e o mais velho tem " + str(maior) + " anos")