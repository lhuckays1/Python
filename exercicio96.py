a = [3]
cont = int(0)

for cont in range(0,10,1):
    a.append((a[cont])*2)

    if(a[cont] == 3 or a[cont] == 6 or a[cont] == 96):
        print(f"${a[cont]}$", end=", ")
    else:
        print(f"{a[cont]}", end=", ")