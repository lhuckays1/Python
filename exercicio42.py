nota1 = float(input("Digite a 1ª nota do aluno: "))
nota2 = float(input("Digite a 2ª nota do aluno: "))
frequencia = int(input("Digite a frequencia do aluno: "))

media = float(nota1 + nota2 / 2)

if(media >= 60 and frequencia >= 75):
    print("aprovado")

if(media >= 40 and media <= 60):
    print("está de recuperação")
    recuperacao = int(input("Digite a nota de recuperação: "))
    if(recuperacao <= 69.99):
        print("Reprovado")
    else:
        print("aprovado")

if(media < 40):
    print("reprovado sem direito a recuperação")