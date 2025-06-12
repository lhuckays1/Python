preco = float(input("Digite o preço do produto: "))
print("Escolha em qual epoca do ano estamos: ")
print("[1] Carnaval")
print("[2] Ferias escolares")
print("[3] Dia das Crianças")
print("[4] Black Friday")
print("[5] Natal")
resp = int(input(""))
precoFinal = float(0)

match resp:
    case 1:
        precoFinal = preco * 1.10
        print("O preço final nessa data é R$" + str(precoFinal))
    case 2:
        precoFinal = preco * 1.20
        print("O preço final nessa data é R$" + str(precoFinal))
    case 3:
        precoFinal = preco * 1.05
        print("O preço final nessa data é R$" + str(precoFinal))
    case 4:
        precoFinal = preco * 0.70
        print("O preço final nessa data é R$" + str(precoFinal))
    case 5:
        precoFinal = preco * 0.95
        print("O preço final nessa data é R$" + str(precoFinal))
    case _:
        print("opção invalida")