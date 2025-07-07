def demitir(salario):
    ferias = float(salario * 1.33)
    total = float(salario + ferias)
    print(f"Você receberá no total R${total:.2f} que inclui o salario do mês mais as suas férias")