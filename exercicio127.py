import exercicio127funcao

resp = str(input("Digite o seu cargo: "))

exercicio127funcao.analisar(resp)

rendaAnual = exercicio127funcao.analisar(resp) * 12

print(f"Sua renda anual é {rendaAnual}")