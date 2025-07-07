cont = int(0)

num = int(input("Digite o número da tabuada que deseja visualizar: "))

for cont in range(0,11,1):
    total = int(num * cont)

    print(f"{num} x {cont} = {total}")