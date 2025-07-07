def analisar(resp):
    if(resp == "policial" or resp == "medico"):
        salario = float(2000)
        print(f"Salario é {salario:.2f}")
    if(resp == "coach" or "magico"):
        salario= float(1500)
        print(f"Salario é {salario:.2f}")
    else:
        salario = float(500)
        print(f"Salario é {salario:.2f}")
    return analisar