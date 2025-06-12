a = int(input("Digite um numero"))

if (a > 10):
    print("deu certo")
else:
    print("deu errado")

if (a > 10 and a < 20):
    print("deu certo 1")
elif(a > 20 or a < 30): #elif equivale a senão se
    print("deu certo")
else:
    print("deu errado")

    import random

    a = random.randint(10,20)

    print(a)