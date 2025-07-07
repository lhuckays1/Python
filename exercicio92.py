francisco = float(1.50)
sara = float(1.10)
cont = int(0)

while (sara < francisco):
    francisco = francisco + 0.02
    sara = sara + 0.03
    cont += 1

print(f"Serão necessarios {cont} anos para que Sara seja maior que Francisco")