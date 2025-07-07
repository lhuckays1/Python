saque = int(input("Digite o valor que deseja sacar: "))
notas50 = int(0)
notas20 = int(0)
notas10 = int(0)
notas2 = int(0)
notas1 = int(0)

print(f"Será realizado o saque de R${saque}")

while (saque >= 50):
    notas50 += 1
    saque = saque - 50

while(saque >= 20):
    notas20 += 1
    saque = saque - 20

while(saque >=10):
    notas10 += 1
    saque = saque - 10

while(saque >= 2):
    notas2 += 1
    saque = saque - 2

while(saque >= 1):
    notas1 += 1
    saque = saque - 1

print(f"{notas50} nota de R$50.00")
print(f"{notas20} nota de R$20.00")
print(f"{notas10} nota de R$10.00")
print(f"{notas2} nota de R$2.00")
print(f"{notas1} nota de R$1.00")

