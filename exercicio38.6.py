tempo = float(input("Digite o tempo que será gasto na viagem: "))
# distancia = float(input("Digite a distancia em KM: "))
velocidade = float(input("Digite a velocidade média: "))

distancia = float(tempo * velocidade)
litros = float(distancia /12)

print("A distancia em KM será " + str(distancia) + " e a quantidade de litros de combustivel necessario será " + str(litros))
