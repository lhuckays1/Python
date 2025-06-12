resposta = str("")

resposta = input("Usa martelo? ")

homemFerro = int(0)
thor = int(0)
capitao = int(0)

if(resposta == "sim"):
    homemFerro += 0
    thor += 1
    capitao += 0
else:
    homemFerro += 1
    thor += 0
    capitao += 0

resposta = input("Usa traje de aço? ")
if(resposta == "sim"):
    homemFerro += 1
    thor += 0
    capitao += 0
else:
    homemFerro +=0
    thor += 1
    capitao += 1

resposta = input("Solta raio pelo martelo? ")
if(resposta == "sim"):
    homemFerro += 0
    thor += 1
    capitao += 0
else:
    homemFerro += 1
    thor += 0
    capitao += 1

resposta = input("É bilionario? ")
if(resposta == "sim"):
    homemFerro += 1
    thor += 0
    capitao += 0
else:
    homemFerro += 0
    thor += 1
    capitao += 1

resposta = input("Usa escudo? ")
if(resposta == "sim"):
    homemFerro += 0
    thor += 0
    capitao += 1
else:
    homemFerro += 1
    thor += 1
    capitao += 0

print("Homem de ferro tem " + str(homemFerro) + " pontos")
print("Thor tem " + str(thor) + " pontos")
print("Capitão America tem " + str(capitao) + " pontos")
