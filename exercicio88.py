cont = int(1)
num = int(input("Digite um número para saber se é primo ou não: "))
primo = int(0)

if(num <= 1):
    print("Impossivel descobrir")

while(cont <= num):
    if(num%cont == 0):
        primo +=1
    
    cont +=1

if(primo == 2):
    print(f"O número {num} é primo")
else:
    print(f"O número {num} não é primo")
