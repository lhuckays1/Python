velocidade = int(input("Qual a velocidade do veiculo? "))

multa = float((velocidade - 80)*10) + 450.00

if(velocidade <= 80):
    print("Velocidade segura")

else:
    print("Limite excedido, sua multa é " + str(multa) + " reais.")