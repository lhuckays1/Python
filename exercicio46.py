compra = float(input("Digite o valor da compra: "))

desconto = float(compra * 0.95)

if(compra > 500):
    print("O valor final da sua compra é " + str(desconto))

else:
    print("O valor final da sua compra é " + str(compra))