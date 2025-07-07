cont = int(0)
marcos = int(0)

for cont in range(0,5,1):
    nome = str(input(f"Digite o {cont+1}º nome: "))
    if(nome == "marcos"):
        marcos +=1

print(f"{marcos} pessoas foram cadastradas com o nome Marcos")
