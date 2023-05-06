def mensagem_jogo(opcao, jogador, computador):
    itens = ["Pedra", "Papel", "Tesoura"]

    if(opcao == 1):
        mensagem = f'''
            {imprime_desenho(jogador)}
            {imprime_desenho(computador)}

            Você: {itens[jogador]} 
            Eu: {itens[computador]} 
            
            Resultado: EMPATE!!'''
    elif(opcao == 2):
        mensagem =  f'''
            {imprime_desenho(jogador)}
            {imprime_desenho(computador)}

            Você: {itens[jogador]} 
            Eu: {itens[computador]} 
            
            Resultado: VOCÊ GANHOU!! =D'''
    else:
        mensagem =  f'''
            {imprime_desenho(jogador)}
            {imprime_desenho(computador)}

            Você: {itens[jogador]} 
            Eu: {itens[computador]} 
            
            Resultado: VOCÊ PERDEU!! =(('''
    return mensagem

def imprime_desenho(opcao):

    if(opcao == 0):
        desenho = f'''
            "      PEDRA      "
            "    _______     "
            "---'   ____)"
            "      (_____)"
            "      (_____)"
            "      (____)"
            "---.__(___)"
            '''
    elif(opcao == 1):
         desenho = f'''
            "       PAPEL   "
            "    _______"
            "---'   ____)____"
            "          ______)"
            "          _______)"
            "         _______)"
            "---.__________)"
            '''
    else:
        desenho = f'''
            "     TESOURA     "
            "    _______"
            "---'   ____)____"
            "          ______)"
            "       __________)"
            "      (____)"
            "---.__(___)"
        '''
    return desenho