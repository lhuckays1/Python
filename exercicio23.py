compra1 = float(input("Digite o valor da 1ª compra: "))
compra2 = float(input("Digite o valor da 2ª compra: "))
compra3 = float(input("Digite o valor da 3ª compra: "))

soma = float(compra1 + compra2 + compra3)

media = float(soma / 3)

if(soma > (media * 2)):
    print("verdadeiro")
else:
    print("falso")