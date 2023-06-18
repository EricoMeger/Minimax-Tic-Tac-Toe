class Minimax():
    def __init__(self):
        self.linhas = 0
        self.melhorJogada = None
        self.tabuleiro = None
        self.jogada = None
        self.IA = None
        self.humano = None

    def getInfo(self, tabuleiro, jogador, linhas, escolha):
        self.IA = jogador
        self.humano = 'O' if self.IA == 'X' else 'X'
        self.tabuleiro = tabuleiro
        self.linhas = linhas


        if escolha == '1':
            print("modo fácil selecionado")
            self.minimaxEasy(self.IA)
        else:
            self.minimax(self.IA)
            
        return self.melhorJogada

    def minimax(self, jogador):
        if self.checkVitoria(self.IA):
            return 10 
        elif self.checkVitoria(self.humano):
            return -10 
        elif self.checkEmpate():
            return 0

        if jogador == self.IA:
            melhorPontuacao = -1000
        else:
            melhorPontuacao = 1000

        melhorJogada = None

        for i in range(self.linhas):
            for j in range(self.linhas):
                if self.tabuleiro[i][j] == '_':
                    self.tabuleiro[i][j] = jogador
                    
                    if jogador == self.IA:
                        pontuacao = self.minimax(self.humano)
                        if pontuacao > melhorPontuacao:
                            melhorPontuacao = pontuacao
                            melhorJogada = [i, j]
                    else:
                        pontuacao = self.minimax(self.IA)
                        if pontuacao < melhorPontuacao:
                            melhorPontuacao = pontuacao
                            melhorJogada = [i, j]

                    self.tabuleiro[i][j] = '_'

        if melhorJogada != None:
            self.melhorJogada = melhorJogada

        return melhorPontuacao
    
    #minimax q nao funciona reaproveitado =)
    def minimaxEasy(self, jogador):
        if self.checkVitoria(jogador) and jogador == self.IA:
            return 10 
        elif self.checkVitoria(jogador) and jogador == self.humano:
            return -10 
        elif self.checkEmpate():
            return 0

        if jogador == self.IA:
            melhorPontuacao = -1000
        else:
            melhorPontuacao = 1000

        melhorJogada = None

        for i in range(self.linhas):
            for j in range(self.linhas):
                if self.tabuleiro[i][j] == '_':
                    self.tabuleiro[i][j] = jogador
                    
                    if jogador == self.IA:
                        pontuacao = self.minimaxEasy(self.humano)
                        if pontuacao > melhorPontuacao:
                            melhorPontuacao = pontuacao
                            melhorJogada = [i, j]
                    else:
                        pontuacao = self.minimaxEasy(self.IA)
                        if pontuacao < melhorPontuacao:
                            melhorPontuacao = pontuacao
                            melhorJogada = [i, j]

                    self.tabuleiro[i][j] = '_'

        if melhorJogada != None:
            self.melhorJogada = melhorJogada

        return melhorPontuacao

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

            for j in range(self.linhas):
                if self.tabuleiro[i][j] == sinal:
                    horizontal.append((i, j))

                if self.tabuleiro[j][i] == sinal:
                    vertical.append((j, i))

            if len(horizontal) == self.linhas or len(vertical) == self.linhas or len(diagonal_principal) == self.linhas or len(diagonal_secundaria) == self.linhas:
                return True
        
        return False
        
    def checkEmpate(self):
        espacos = []
        for i in range(self.linhas):
            for j in range(self.linhas):
                if self.tabuleiro[i][j] == '_':
                    espacos.append(self.tabuleiro[i][j])

        if len(espacos) == 0:
            return True
        else:
            return False


            
