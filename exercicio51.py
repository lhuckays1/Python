peso = float(input("Digite seu peso: "))

print("Escolha um planeta: ")
print("[1] Mercurio")
print("[2] Venus")
print("[3] Marte")
print("[4] Jupiter")
print("[5] Saturno")
print("[6] Urano")
resp = int(input(""))
pesoFinal = float(0)

match resp:
    case 1:
        pesoFinal = peso * 0.37
        print("Se você estivesse no planeta Mercurio você pesaria " + str(pesoFinal))
    case 2:
        pesoFinal = peso * 0.88
        print("Se você estivesse no planeta Venus você pesaria " + str(pesoFinal))
    case 3:
        pesoFinal = peso * 0.38
        print("Se você estivesse no planeta Marte você pesaria " + str(pesoFinal))
    case 4:
        pesoFinal = peso * 2.64
        print("Se você estivesse no planeta Jupiter você pesaria " + str(pesoFinal))
    case 5:
        pesoFinal = peso * 1.15
        print("Se você estivesse no planeta Saturno você pesaria " + str(pesoFinal))
    case 6:
        pesoFinal = peso * 1.17
        print("Se você estivesse no planeta Urano você pesaria " + str(pesoFinal))
    case _:
        print("Opção Invalida")