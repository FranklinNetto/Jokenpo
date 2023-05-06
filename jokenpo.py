import random
import mensagens
import os
import time


def escolha_computador():
    escolha = int(random.randrange(0,3))
    return escolha

def jogar(opcao):
    jogador_opcao = opcao-1

    computador_opcao = escolha_computador()

    if(jogador_opcao == computador_opcao):
        resultado = mensagens.mensagem_jogo(1, jogador_opcao, computador_opcao)
    elif(jogador_opcao == 0 and computador_opcao == 2) or \
        (jogador_opcao == 1 and computador_opcao == 0) or \
        (jogador_opcao == 2 and computador_opcao == 1):
        resultado = mensagens.mensagem_jogo(2, jogador_opcao, computador_opcao)
    else:
        resultado = mensagens.mensagem_jogo(3, jogador_opcao, computador_opcao)

    print(resultado)
    time.sleep(3)
    limpar_tela()
    iniciar_jogo()


def iniciar_jogo():
    print("##################################################")
    print("Bem vindo ao jogo Jokenpô (pedra, papel e tesoura)")
    print("##################################################")
    print("\n")

    escolha = input( f'''
    >>> Escolha:
        > 1 - Pedra
        > 2 - Papel
        > 3 - Tesoura
        > 4 - Para sair do jogo
    :  ''')
    validacao_jogo(escolha)

def validacao_jogo(opcao):
    try:
        opcao = int(opcao)
    except ValueError:
        print("DIGITE SOMENTE NÚMEROS")
        limpar_tela()
        iniciar_jogo()

    while (opcao != 4):
        if (opcao <  0 or opcao >= 5):
            print("Opção inválida!")
            limpar_tela()
            iniciar_jogo()
            continue
        else:
            jogar(opcao)

    limpar_tela()
    print("Obrigado, volte sempre!! ^^_")
    print("<<<< FIM DO JOGO >>>>")

def limpar_tela():
    if (os.name == 'nt'):
        time.sleep(2)
        os.system('cls')
    else:
        time.sleep(2.0)
        os.system('clear')

iniciar_jogo()