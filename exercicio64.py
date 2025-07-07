contador = int(0)
homemVelho = str("")
mulherJovem = str("")
maior = int(0)
menor = int(99999)

while (contador != 5):
    nome = str(input(f"Digite o {contador + 1} nome: "))
    sexo = str(input("Digite o sexo: "))
    idade = int(input("Digite a idade: "))
    
    if(idade > maior and sexo == "masculino"):
        maior = idade
        homemVelho = nome
    if(sexo == "feminino" and idade < menor):
        menor = idade
        mulherJovem = nome
    contador +=1
    
print(f"O nome do homem mais velho é {homemVelho} e nome da mulher mais jovem é {mulherJovem}")
