num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

print("Escolha qual operação deseja realizar:")
print("[1] Soma")
print("[2] Subtração")
print("[3] Multiplicação")
print("[4] Divisão")
resp = int(input(""))

match resp:
    case 1:
        soma = int(num1 + num2)
        print("A Soma dos números é " + str(soma))
    case 2:
        subtracao = int(num1 - num2)
        print("A Subtracação dos números é " + str(subtracao))
    case 3:
        multiplicacao = int(num1 * num2)
        print("A Multiplicação dos números é " + str(multiplicacao))
    case 4:
        divisao = int(num1 / num2)
        print("A Divisão dos números é " + str(divisao))
    case _:
        print("Opção Invalida")
