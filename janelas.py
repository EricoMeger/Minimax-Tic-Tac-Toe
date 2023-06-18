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

    def IAChoiceScreen(self):
        print("==============================================")
        print("|                 VOCÊ DESEJA...             |")
        print("==============================================")
        print("|              1 - Modo fácil                |")
        print("|(De vez em quando a IA fará jogadas erradas)|")
        print("|              2 - Modo difícil              |")
        print("|   (Você só conseguirá perder ou empatar)   |")
        print("==============================================")
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