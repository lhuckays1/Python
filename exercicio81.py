cont = int(0)
soma = int(0)

for cont in range(0,9,1):
    num = int(input("Digite um número: "))
    if(num == 999):
        print("Foi digitado o número correto 999")
        break
    soma = soma + num

print(f"Foi realizado {cont+1} tentativas")
print(f"A soma dos números digitados é: {soma}")

