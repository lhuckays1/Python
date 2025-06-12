print("Escolha qual a serie você assistiu esse final de semana:")
print("[1] Sandman")
print("[2] Wandinha")
print("[3] Game Of Thrones")
print("[4] Dota")
print("[5] Dexter")
serie = int(input(""))

match serie:
    case 1:
        print("A serie escolhida foi Sandman")
    case 2:
        print("A serie escolhida foi Wandinha")
    case 3:
        print("A serie escolhida foi Game Of Thrones")
    case 4:
        print("A serie escolhida foi Dota")
    case 5:
        print("A serie escolhida foi Dexter")
    case _:
        print("Opção Invalida")