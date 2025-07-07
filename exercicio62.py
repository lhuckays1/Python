pesoMedio = float(78.5)
contador = int(0)
pesoAcima = int(0)
pesoAbaixo = int(0)

while (contador != 4):
    peso = float(input(f"Digite o peso da {contador + 1}ª pessoa: "))
    if(peso > pesoMedio):
        pesoAcima = pesoAcima + 1
    if(peso <= pesoMedio):
        pesoAbaixo = pesoAbaixo + 1
    contador += 1

print(f"Existe {pesoAcima} pessoas que estão acima do peso médio e existe {pesoAbaixo} pessoas com peso igual ou abaixo da média")
    