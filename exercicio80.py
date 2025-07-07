cont = int(0)

for cont in range(0,3,1):
    num = int(input("Digite um número: "))
    if(num == 20):
        break

if(cont == 3):
    print("Programa finalizado, devido número maximo de tentativas atingido")