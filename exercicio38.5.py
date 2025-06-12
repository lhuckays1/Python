aulas = int(input("Digite a quantidade de aula lecionadas no mês: "))

salario = float(aulas * 40)
inss = float(0)
salarioFinal = float(0)
salarioAtual = float(0)

if(salario >= 0 and salario <= 1518.00):
    inss = salario * 0.075
    salarioFinal = salario - inss
    print("O seu desconto do INSS será R$" + str(inss) + " e seu salario será R$" + str(salarioFinal))
else:
    salarioAtual = salario - 1518.00

if(salario >= 1518.01 and salario <= 2793.88):
    inss = (1518.00 * 0.075) + (salarioAtual * 0.09) - 22.77
    salarioFinal = salario - inss
    print("O seu desconto do INSS será R$" + str(inss) + " e seu salario será R$" + str(salarioFinal))
else:
    salarioAtual = salarioFinal - 2793.88

if(salario >= 2793.89 and salario <= 4190.83):
    inss = (1518.00 * 0.075) + (2793.00 * 0.09) + (salarioAtual * 0.12) - 106.59
    salarioFinal = salario - inss
    print("O seu desconto do INSS será R$" + str(inss) + " e seu salario será R$" + str(salarioFinal))
else:
    salarioAtual = salarioFinal - 4190.83

if(salario >= 4190.84 and salario <= 8157.41):
    inss = (1518.00 * 0.075) + (2793.00 * 0.09) + (4190.83 * 0.12) + (salarioAtual * 0.14) - 190.40
    salarioFinal = salario - inss
    print("O seu desconto do INSS será R$" + str(inss)+ " e seu salario será R$" + str(salarioFinal))

