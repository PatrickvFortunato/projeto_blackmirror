opcaoEscolhida = -1

while(opcaoEscolhida != 0):
    opcaoEscolhida = (input(f'''
    ======== Q U E S T I O N Á R I O =============================================================
    ESCOLHA UMA DAS PERGUNTAS ABAIXO E DIGITE EXATAMENTE COMO ESTÁ(TUDO MAIUSCULO): 
    QUAL É O NOME COMPLETO DA PROTAGONISTA DO EPISÓDIO?
    QUEM DIRIGE A VIDA DE JOAN EM TEMPO REAL PARA UMA SÉRIE DE TELEVISÃO?
    QUAL É O NOME DO SERVIÇO DE STREAMING FICTÍCIO QUE PARODIA A NETFLIX NO EPISÓDIO?
    COMO JOAN DESCOBRE A EXISTÊNCIA DA SÉRIE SOBRE SUA VIDA?
    QUAL É A REAÇÃO INICIAL DE JOAN AO DESCOBRIR A SÉRIE E O QUE ELA FAZ EM RESPOSTA?
    QUAIS SÃO OS TEMAS PRINCIPAIS EXPLORADOS NESTE EPISÓDIO DE BLACK MIRROR?
    O EPISÓDIO TERMINA DE MANEIRA TÍPICA PARA A SÉRIE BLACK MIRROR? EXPLIQUE
    
    SAIR
    ============================================================================================
    : '''))
    if (opcaoEscolhida == 'QUAL É O NOME COMPLETO DA PROTAGONISTA DO EPISÓDIO?'):
        print("ChatPTK: Joan is Awful ")
    elif (opcaoEscolhida == 'QUEM DIRIGE A VIDA DE JOAN EM TEMPO REAL PARA UMA SÉRIE DE TELEVISÃO?' ):
         print("ChatPTK: Salma Hayek ")
    elif(opcaoEscolhida == 'QUAL É O NOME DO SERVIÇO DE STREAMING FICTÍCIO QUE PARODIA A NETFLIX NO EPISÓDIO?'):
        print("ChatPTK: Streamberry ")
    elif (opcaoEscolhida == 'COMO JOAN DESCOBRE A EXISTÊNCIA DA SÉRIE SOBRE SUA VIDA?' ):
         print("ChatPTK: Quando parou pra assistir uma série com seu marido, e percebeu que se tratava sobre ela ")
    elif(opcaoEscolhida == 'QUAL É A REAÇÃO INICIAL DE JOAN AO DESCOBRIR A SÉRIE E O QUE ELA FAZ EM RESPOSTA?'):
        print("ChatPTK: Ficou em choque, achando que era uma pegadinha do marido. ")
    elif (opcaoEscolhida == 'QUAIS SÃO OS TEMAS PRINCIPAIS EXPLORADOS NESTE EPISÓDIO DE BLACK MIRROR?' ):
         print("ChatPTK: Como CGI e a inteligência artificial podem destruir a vida de alguém ")
    elif(opcaoEscolhida == 'O EPISÓDIO TERMINA DE MANEIRA TÍPICA PARA A SÉRIE BLACK MIRROR? EXPLIQUE'):
        print("ChatPTK: Infelizmente não temos uma resposta ainda.")
    elif(opcaoEscolhida == 'SAIR'):
        print("@@SAINDO DO APP...@@")


        break
    else:
        print("!!! O P Ç Ã O  I N V A L I D A !!!")