distancia = float(input("Digite a distancia da corrida: "))

valor = float(0)

if(distancia <= 200):
    valor = (distancia * 0.35)
    perigo = str(input("O destino é perigoso? "))
    if(perigo == "sim"):
        valor = (valor * 2)
        print("O valor final da corrida para o destino escolhido é " + str(valor) + " reais")
    else:
        print("O valor final da corrida para o destino escolhido é " + str(valor) + " reais")
else:
    valor = (distancia * 0.20)
    perigo = str(input("O destino é perigoso? "))
    if(perigo == "sim"):
        valor = (valor * 1.8)
        print("O valor final da corrida para o destino escolhido é " + str(valor) + " reais")
    else:
        print("O valor final da corrida para o destino escolhido é " + str(valor) + " reais")

