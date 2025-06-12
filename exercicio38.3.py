valor = float(input("Digite o valor do produto: "))
resposta = int(input("Digite o código de condição de pagamento: \n[1]À vista em dinheiro ou pix \n[2]À vista no cartão de crédito \n[3]Parcelado no cartão em duas vezes \n[4]Parcelado no cartão em três vezes ou mais \n"))
parcelas = float(0)
valorFinal = float(0)

if (resposta == 1):
    valor = valor - (valor * 0.15)
    print("O valor final do produto é " + str(valor))

elif (resposta == 2):
    valor = valor - (valor * 0.10)
    print("O valor final do produto é " + str(valor))
    
elif (resposta == 3): 
    valor = valor
    parcelas = 2
    valorFinal = valor / parcelas
    print("O valor final do produto é " + str(valor) + " e será pago em " + str(parcelas) + " parcelas de " + str(valorFinal))
elif (resposta == 4):
    respostaParcelas = int(input("Digite o número de parcelas: "))
    valor = valor + (valor * 0.10)
    parcelas = respostaParcelas
    valorFinal = valor / parcelas
    print("O valor final do produto é " + str(valor) + " e será pago em " + str(parcelas) + " parcelas de " + str(valorFinal))
else:
    print("Código de condição de pagamento inválido")