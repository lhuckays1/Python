salario = float(input("Digite o salario: "))

ferias = float(salario * 1.33)
bonus = float(salario * 0.74)
promocao = float(salario * 1.45)

print("Baseado no seu salario suas férias seriam R$" + str(ferias) + ", seu bônus seria R$" + str(bonus) + " e caso você fosse promovida seria R$" + str(promocao))