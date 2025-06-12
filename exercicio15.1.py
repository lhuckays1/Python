km = float(input("Digite a distancia percorrida em KM: "))
dias = int(input("Qual a quantidade de dias alugado? "))

pagar = float((km * 0.15) + (dias * 60))

print("O valor total a pagar é " + str(pagar) + " reais")