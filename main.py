#Adicionar a "IA" para jogar, seguindo aquele algoritmo de minimax
from janelas import Screens
from minimax import Minimax
import os
import platform

class JogoVelha():
    def __init__(self):
        self.tabuleiro = []
        self.jogador1 = None
        self.jogador2 = None
        self.linhas = 0
        self.colunas = 0
        self.vez = 0
        self.janela = Screens()
        self.minimax = Minimax()
        self.vezIA = False

    def criaTabuleiro(self):
        escolha = input("Qual será o tamanho do tablado? Insira no formato '3x3' ")
        try:
            self.linhas, self.colunas = map(int, escolha.split('x'))
            if self.linhas != self.colunas:
                print("O tabuleiro deve ser quadrado! (Linhas e Colunas devem ser equivalentes.)")
                quit()
        except ValueError:
            print("Utilize o formato 'Número 'x' Número' !!!")
            quit()

        self.tabuleiro = [['_'] * self.colunas for i in range(self.linhas)]

    def checkVitoria(self, sinal):
        diagonal_principal = []
        diagonal_secundaria = []
        for i in range(self.linhas):
            horizontal = []
            vertical = []
            if self.tabuleiro[i][i] == sinal:
                diagonal_principal.append((i, i))
            
            if self.tabuleiro[i][self.linhas - i - 1] == sinal:
                    diagonal_secundaria.append((i, self.linhas - i - 1))

            for j in range(self.colunas):
                if self.tabuleiro[i][j] == sinal:
                    horizontal.append((i, j))

                if self.tabuleiro[j][i] == sinal: #Isso só funciona pq o tabuleiro é quadrado..
                    vertical.append((j, i))

            #peço perdão pelo crime cometido abaixo   
            if len(horizontal) == self.linhas or len(vertical) == self.colunas or len(diagonal_principal) == self.linhas or len(diagonal_secundaria) == self.linhas:
                self.janela.victoryScreen(sinal)
                quit()  
        
        #Multiplicando as linhas e colunas do tabuleiro nos permite saber o máximo de jogadas que podem ocorrer.
        if self.vez == (self.linhas*self.colunas):
            self.janela.velhaScreen()
            quit()        

    def mostraTabuleiro(self):
        self.clearTerminal()
        for i in self.tabuleiro:
            print(' '.join(i))
        print('\n')
    
    def marcaJogada(self, jogada, sinal):
        if not self.vezIA:
            try: 
                linha, coluna = map(int, jogada.split())
            except ValueError:
                print("Insira no formato 1 1, com sua linha e coluna sendo separadas por um espaço.")
                return
            
            try:
                if self.tabuleiro[linha - 1][coluna - 1] != '_':
                    print("Posição já marcada!")
                    return
                else:
                    self.tabuleiro[linha - 1][coluna - 1] = sinal
            except IndexError:
                print(f"Insira uma posição válida, de 1 até {self.linhas}")
                return
        else:
            self.tabuleiro[jogada[0]][jogada[1]] = sinal
        
        self.vezIA = False
        self.vez += 1
        self.mostraTabuleiro()

    def clearTerminal(self):
        sistema = platform.system().lower()
        if 'windows' in sistema:
            os.system('cls')
        else:
            os.system('clear')

    def main(self):
        escolha = self.janela.initScreen()
       
        if escolha != '1':
            print("Entendemos que você quer sair!")
            quit()

        self.criaTabuleiro()

        escolha = input("Digite '1' para jogar contra outro jogador e '2' para jogar contra a máquina: ")
        if escolha == '2' and self.linhas > 3:
            print("Desculpe! Limitamos a jogada contra IA para 3x3.")
            quit()
        
        elif escolha == '2':
            dificuldade = self.janela.IAChoiceScreen()

        sinal = input("Jogador 1 deseja ser X ou O? ")
        self.clearTerminal() 

        self.jogador1 = 'X' if sinal.lower() == 'x' else 'O' #'Ternário' em Python
        self.jogador2 = 'O' if self.jogador1 == 'X' else 'X'
        
        self.mostraTabuleiro()
        print("Lembre-se, o tabuleiro é uma matriz, escolha uma linha e uma coluna: 1 1, por exemplo, irá marcar o primeiro quadrado. ")

        while True:
            if self.vez % 2 == 0:
                jogador = self.jogador1
                print(f"\nVez de jogador {jogador}\n")
                jogada = input(f"{jogador}, em qual posição você deseja marcar? ")
            else:
                jogador = self.jogador2
                print(f"\nVez de jogador {jogador}\n")
                if escolha == '1': 
                    jogada = input(f"{jogador}, em qual posição você deseja marcar? ")
                else:
                    jogada = self.minimax.getInfo(self.tabuleiro, self.jogador2, self.linhas, dificuldade)
                    self.vezIA = True
                  
            self.marcaJogada(jogada, jogador)
            self.checkVitoria(jogador)

a = JogoVelha()
a.main()
