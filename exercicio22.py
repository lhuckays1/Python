idade = int(input("Digite sua idade: "))
ingles = str(input("Você fala inglês? "))

if(idade > 25 and ingles == "sim"):
    print("Verdadeiro")
elif(ingles == "sim"):
    print("Verdadeiro")
elif(idade > 25 and ingles == "não"):
    print("Falso")
else:
    print("Falso")