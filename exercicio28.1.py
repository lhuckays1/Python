velocidade = int(input("Digite a velocidade do veiculo: "))
multa = float(0
              )
if(velocidade <= 80):
    print("Velocidade segura")

if((velocidade - 80) > 0 and (velocidade - 80) <= 20):
    multa = ((velocidade - 80) * 5.00) + 150.00
    print("Limite de velocidade excedido. Sua multa é " + str(multa) + " reais")

if((velocidade - 80) > 21 and (velocidade - 80 ) <= 80):
    multa = ((velocidade - 80) * 10.00) + 250.00
    print("Limite de velocidade excedido. Sua multa é " + str(multa) + " reais")

if((velocidade - 80) > 81 and (velocidade - 80) <= 200):
    multa = ((velocidade - 80) * 20.00) + 500.00
    print("Limite de velocidade excedido. Sua multa é " + str(multa) + " reais")

if((velocidade - 80) > 201):
    print("Veiculo será confiscado")