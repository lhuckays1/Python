peso = float(input("Digite seu peso em kg: "))
sanduiches = int(input("Quantos sanduiches comeu esse mês? "))

novoPeso = float((sanduiches * 0.10) + peso)

gasto = float(sanduiches * 8.50)

print("O novo peso é " + str(novoPeso) + " e o valor gasto com sanduiches foi " + str(gasto))