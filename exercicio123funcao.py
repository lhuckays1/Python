def aVista(venda):
    total = float(venda * 0.9)
    print(f"O valor final da venda é {total:.2f}")

def aPrazo(venda):
    total = float(venda * 1.1)
    print(f"O valor final da venda é {total:.2f}")

def cartao(venda):
    parcela = int(input("Digite em quantas vezes deseja parcelar: "))
    total_parcela = float(venda * 1.20) / parcela
    total = float(venda * 1.20)
    print(f"O valor final da venda é {total:.2f} parecelado em {parcela} vezes de R${total_parcela:.2f}")