conta = float(input("Qual o valor em reais você tem na conta? "))

dolares = float(conta * 0.18)
euros = float(conta * 0.15)
iene = float(conta * 25.14)

print("Você tem equivalente a " + str(dolares) + " dolares")
print("Você tem equivalente a " + str(euros) + " euros")
print("Você tem equivalente a " + str(iene) + " iene")