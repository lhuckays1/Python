import exercicio125funcao

num = int(input("Digite um número: "))
dobrar = exercicio125funcao.dobrar(num)

num = int(input("Digite outro número: "))

soma = int(dobrar + num)

print(f"A soma do valor {dobrar} + {num} é: {soma}")