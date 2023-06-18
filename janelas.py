import os 

class Screens():
    def __init__(self):
        pass

    def initScreen(self):
        os.system('clear')
        print("====================================")
        print("|         JOGO DA VELHA            |")
        print("====================================")
        print("|          1 - Iniciar jogo        |")
        print("|          2 - Sair                |")
        print("====================================")
        a = input("Escolha uma opção: ")

        return a

    def victoryScreen(self, jogador):
        print("\n         === JOGO DA VELHA ===")
        print("\n==-==-==-==-==-==-==-==-==-==-==-==-==")
        print("|                                    |")
        print("|               VITÓRIA              |")
        print(f"|             do jogador {jogador}           |")
        print("|                                    |")
        print("==-==-==-==-==-==-==-==-==-==-==-==-==")

    def velhaScreen(self):
        print("====================================")
        print("|           DEU VELHA!             |")
        print("====================================")