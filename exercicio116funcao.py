def lascado(resp):
    divida = float(input("Digite o valor da sua divida: "))
    tempo = int(input("Digite o tempo dessa divida: "))
    taxa = float(input("Digite qual a taxa de juros: "))
    juros = float(divida * tempo * taxa)
    total = float(divida + juros)
    print(f"Você vai pagar um total de R${juros:.2f} de juros e o valor total da divida será {total:.2f}")
