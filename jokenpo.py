import random
import os
import time

def iniciar_jogo():
    print("##################################################")
    print("Bem vindo ao jogo Jokenpô (pedra, papel e tesoura)")
    print("##################################################")
    print("\n")

    print("**Escolha:**")
    print("     1 - Pedra")
    print("     2 - Papel")
    print("     3 - Tesoura")
    print("     9 - Para sair")
    print("\n")

    while (aposta_jogador != 9):
        aposta_jogador = int(input())

        if (aposta_jogador < 0 or aposta_jogador > 4):
            print("Opção Inválida")
            break
        else:
            print("Você escolheu:  {} - {}".format(aposta_jogador, logica_jogo(aposta_jogador)))

        aposta_jogo = palpite_jogo()
        print("O jogo escolheu: {} - {}".format(aposta_jogo, logica_jogo(aposta_jogo)))
        time.sleep(2.0)

def logica_jogo(palpite):
    itens = {1 : "Pedra", 2: "Papel", 3: "Tesoura"}

    item = itens[palpite]

    return item

def palpite_jogo():
    chance = random.randrange(1,4)
    print(chance)

    return chance


def limpar_tela():
    if (os.name == 'nt'):
        os.system('cls')
    else:
        os.system('clear')


limpar_tela()
iniciar_jogo()
