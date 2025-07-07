contador = int(0)
cat1 = int(0)
cat2 = int(0)
cat3 = int(0)
cat4 = int(0)


while (contador != 9999):
    num = int(input("Digite um número: "))

    if(num >= 0 and num <= 25):
        cat1 +=1
    elif(num >= 26 and num <=50):
        cat2 +=1
    elif(num >=51 and num <=75):
        cat3 +=1
    elif(num >=76 and num <= 100):
        cat4 +=1
    
    contador +=1
    resp = str(input("Deseja continuar digitando mais números? "))
    if(resp == "nao"):
        break

print(f"{cat1} números estão entre [0-25]")
print(f"{cat2} números estão entre [26-50]")
print(f"{cat3} números estão entre [51-75]")
print(f"{cat4} números estão entre [76-100]")
