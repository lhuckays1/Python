time = str(input("Qual time de futebol você torce? "))

if(time == "atletico"):
    uniforme = int(input("Qual uniforme você prefere? \n[1] Modelo 1 \n[2] Modelo 2 \n"))

    if(uniforme == 1):
        print("O valor será de R$85,00")
    if(uniforme ==2):
        print("O valor será de R$75,00")

if(time == "cruzeiro"):
    uniforme = int(input("Qual uniforme você prefere? \n[1] Modelo 1 \n[2] Modelo 2 \n"))

    if(uniforme == 1):
        print("O valor será de R$45,00")
    if(uniforme == 2):
        print("O valor será de R$95,00")