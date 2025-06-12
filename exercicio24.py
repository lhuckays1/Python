num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
soma = int(num1 + num2)
media = int(soma / 2)

pergunta = str(input("Deseja saber a soma ou a média dos números? "))

if(pergunta == "soma"):
    print("A soma de " + str(num1) + " + " + str(num2) + " é igual a " + str(soma))
if(pergunta == "media"):
    print("A média de " + str(num1) + " + " + str(num2) + " é igual a " + str(media))