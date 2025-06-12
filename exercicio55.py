print("Escolha a opção que corresponde o seu nivel de conhecimento no excel: ")
print("[1] Basico")
print("[2] Intermediario")
print("[3] Avançado")
resp = int(input(""))

match resp:
    case 1:
        print("Escolha uma formula dentre as opções abaixo:")
        print("[1] SOMA")
        print("[2] MÉDIA")
        print("[3] MÁXIMA")
        basico = int(input(""))

        match basico:
            case 1:
                print("SOMA -> =SOMA(número1;[número2];...)")
            case 2:
                print("MÉDIA -> =MÉDIA(núm1, [núm2], ...)")
            case 3:
                print("MAXIMO -> =MÁXIMO(número1, [número2], ...)")
    
    case 2:
        print("Escolha uma formula dentre as opções abaixo:")
        print("[1] SE")
        print("[2] SOMASE")
        print("[3] CONT.SE")
        intermediario = int(input(""))

        match intermediario:
            case 1:
                print("SE -> =SE(teste_lógico;[valor_se_verdadeiro];[valor_se_falso])")
            case 2:
                print("SOMASE -> =SOMASE(intervalo; critérios; [intervalo_soma])")
            case 3:
                print("CONT.SE -> =CONT.SE(intervalo, critérios)")
    
    case 3:
        print("Escolha uma formula dentre as opções abaixo:")
        print("[1] ORDEM.EQ")
        print("[2] PROCV")
        print("[3] PROCH")
        avancado = int(input(""))

        match avancado:
            case 1:
                print("ORDEM.EQ -> =ORDEM.EQ(núm; ref; [ordem])")
            case 2:
                print("PROCV -> =PROCV(valor_procurado; matriz_tabela; núm_índice_coluna; [procurar_intervalo])")
            case 3:
                print("PROCH -> =PROCH(valor_procurado; matriz_tabela; núm_índice_lin; [procurar_intervalor]")