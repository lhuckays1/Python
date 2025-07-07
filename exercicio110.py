import exercicio110funcao
a = int(input("Digite um número: "))
b = int(input("Digite um número: "))

resp = int(input("Escolha opção referente a operação matematica que deseja realizar: \n[1] Adição \n[2] Subtração \n[3] Multiplicação \n[4] Divisão \n"))

match resp:
    case 1:
        exercicio110funcao.adicao(a,b)
    
    case 2:
        exercicio110funcao.subtracao(a,b)
    
    case 3:
        exercicio110funcao.multiplicacao(a,b)
    
    case 4:
        exercicio110funcao.divisao(a,b)

    case _:
        print("Opção Invalida")