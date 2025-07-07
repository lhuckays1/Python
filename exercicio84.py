cont = int(0)
clienteA = int(0)
clienteB = int(0)
clienteC = int(0)

for cont in range(0,4,1):
    nome = str(input("Digite o nome do produto: "))
    valor = float(input("Digite o valor do produto: "))

    if(valor > 1000.00):
        clienteA += 1
    if(valor >=500.00 and valor <=999.99):
        clienteB += 1
    if(valor <=499.99):
        clienteC += 1

    resp = int(input("Deseja adicionar mais compras? \n[1] Sim \n[2] Não \n"))
    if(resp == 2):
        break

print(f"{clienteA} clientes são padrão A")
print(f"{clienteB} clientes são padrão B")
print(f"{clienteC} clientes são padrão C")
