venda = float(input("Digite o valor total de vendas: "))
comissao = float(0)

if(venda >= 22000):
   ano = int(input("Digite quantos anos ja está na empresa: "))
   if(ano == 2):
      comissao = venda * 0.03
      print("O valor da comissão será R$" + str(comissao))
    
   if(ano >= 3):
      comissao = venda * 0.04
      print("O valor da comissão será R$" + str(comissao))

   if(ano < 2):
      comissao = venda * 0.02
      print("O valor da comissão será R$" + str(comissao))