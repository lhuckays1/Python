casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o salario da pessoa: "))
meses = int(input("Digite em quantos meses ela deseja pagar: "))

prestacao = float(casa / meses)

if(prestacao > (salario * 0.3)):
    print("Emprestimo negado, valor da prestação ultrapassa 30% do salario")

else:
    print("Emprestimo aprovado, o valor da prestação será R$" + str(prestacao))