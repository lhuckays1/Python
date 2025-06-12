produto = float(input("Qual o valor do produto? "))
desconto = float(input("Qual o desconto em %? "))

desconto1 = float(desconto / 100)

total = float(produto - (produto * desconto1))

print("O produto custava " + str(produto) + " mas teve desconto de " + str(desconto) + "% por isso agora está custando " + str(total) + " reais")