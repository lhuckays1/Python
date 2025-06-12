idade1 = int(input("Digite a idade da 1ª pessoa: "))
idade2 = int(input("Digite a idade da 2ª pessoa: "))
pessoa1 = str("")
pessoa2 = str("")

if(idade1 <= 9):
    pessoa1 = "mirim"
elif(idade1 >=10 and idade1 <= 14):
    pessoa1 = "infantil"
elif(idade1 >= 15 and idade1 <= 18):
    pessoa1 = "jovem"
elif(idade1 >= 19 and idade1 <= 24):
    pessoa1 = "adulto"


if(idade2 <= 9):
    pessoa2 = "mirim"
elif(idade2 >= 10 and idade2 <= 14):
    pessoa2 = "infantil"
elif(idade2 >=15 and idade2 <= 18):
    pessoa2 = "jovem"
elif(idade2 >= 19 and idade2 <= 24):
    pessoa2 = "adulto"

if(pessoa1 == pessoa2):
    horario = str(input("Digite o horario da luta: "))
    print("Está marcado a luta de uma pessoa com " + str(idade1) + " anos e outra pessoa com " + str(idade2) + " anos na hora " + str(horario))

else:
    print("luta cancelada")