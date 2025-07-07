contador = int(0)
num = int(input("Digite o número da tabuada que deseja visualizar: "))
resultado = int(0)

while (contador != 11):
    resultado = num * contador
    print(f"{num} x {contador} = {resultado}")
    contador += 1
