cont = int(0)
mais10 = int(0)
contHomens = int(0)
contMulheres = int(0)

for cont in range (0,4,1):
    idade = int(input("Digite a idade do usuario: "))
    sexo = int(input("Escolha o sexo do usuario: \n[1] Masculino \n[2] Feminino \n"))

    if(idade > 10):
        mais10 += 1
    
    if(sexo == 1):
        contHomens +=1
    
    if(sexo == 2 and idade < 20):
        contMulheres +=1

print(f"{mais10} pessoas tem mais de 10 anos")
print(f"{contHomens} homens foram cadastrados")
print(f"{contMulheres} mulheres com menos de 20 anos foram cadastradas")

