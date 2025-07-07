import exercicio123funcao

venda = float(input("Digite o valor da venda: "))

resp = int(input("Escolha opção de pagamento: \n[1] A vista \n[2] A prazo \n[3] Cartão \n"))

match resp:
    case 1:
        exercicio123funcao.aVista(venda)
    
    case 2:
        exercicio123funcao.aPrazo(venda)
    
    case 3:
        exercicio123funcao.cartao(venda)
    
    case _:
        print("Opção Invalida")