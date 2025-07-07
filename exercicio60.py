num = int(input("Digite até qual número deseja contar: "))
contador = int(0)

while (contador != num):
    contador += 1
    print(" {} --".format(contador), end="")

    if(contador%3 == 0):
        print("PIN \n")

