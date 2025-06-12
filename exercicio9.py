divida = float(input("Qual o valor da divida? "))
tempo = int(input("Qual o tempo em meses? "))
taxa = float(input("Qual a taxa mensal ?"))

juros = float(divida * tempo * taxa)

total = float(juros + divida)

print("Os juros são " + str(juros) + " e o total será de " + str(total))