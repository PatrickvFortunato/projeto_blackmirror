opcaoEscolhida = -1

while(opcaoEscolhida != 0):
    opcaoEscolhida = int(input(f'''
    ======== Q U E S T I O N Á R I O =============================================================
    ESCOLHA UMA DAS PERGUNTAS ABAIXO: 
    [ 1 ] - QUAL É O NOME COMPLETO DA PROTAGONISTA DO EPISÓDIO?
    [ 2 ] - QUEM DIRIGE A VIDA DE JOAN EM TEMPO REAL PARA UMA SÉRIE DE TELEVISÃO?
    [ 3 ] - QUAL É O NOME DO SERVIÇO DE STREAMING FICTÍCIO QUE PARODIA A NETFLIX NO EPISÓDIO?
    [ 4 ] - COMO JOAN DESCOBRE A EXISTÊNCIA DA SÉRIE SOBRE SUA VIDA?
    [ 5 ] - QUAL É A REAÇÃO INICIAL DE JOAN AO DESCOBRIR A SÉRIE E O QUE ELA FAZ EM RESPOSTA?
    [ 6 ] - QUAIS SÃO OS TEMAS PRINCIPAIS EXPLORADOS NESTE EPISÓDIO DE BLACK MIRROR?
    [ 7 ] - O EPISÓDIO TERMINA DE MANEIRA TÍPICA PARA A SÉRIE BLACK MIRROR? EXPLIQUE
    ============================================================================================
    : '''))
    if (opcaoEscolhida == 1):
        print("ChatPTK: Joan is Awful ")
    elif (opcaoEscolhida == 2 ):
         print("ChatPTK: Salma Hayek ")
    elif(opcaoEscolhida == 3):
        print("ChatPTK: Streamberry ")
    elif (opcaoEscolhida == 4 ):
         print("ChatPTK: Quando parou pra assistir uma série com seu marido, e percebeu que se tratava sobre ela ")
    elif(opcaoEscolhida == 5):
        print("ChatPTK: Ficou em choque, achando que era uma pegadinha do marido. ")
    elif (opcaoEscolhida == 6 ):
         print("ChatPTK: Como CGI e a inteligência artificial podem destruir a vida de alguém ")
    elif(opcaoEscolhida == 7):
        print("ChatPTK: Infelizmente não temos uma resposta ainda.")
    elif(opcaoEscolhida == 0):
        print("@@SAINDO DO APP...@@")


        break
    else:
        print("!!! O P Ç Ã O  I N V A L I D A !!!")