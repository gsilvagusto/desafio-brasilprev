class Comportameto:
    def __init__(self, jogador, posicao, probabilidade_50) -> None:
        from app.bo.bo_jogador import JogadorBo
        from app.bo.bo_tabuleiro import Tabuleiro

        self.jogador_bo = JogadorBo
        self.jogador = jogador
        self.posicao = posicao
        self.propriedade = Tabuleiro.tabuleiro
        self.probabilidade_50 = probabilidade_50

    def impulsivo(self):
        # O jogador impulsivo compra qualquer propriedade sobre a qual ele parar.
        msg = self.jogador_bo.comprar(self.jogador, self.posicao)
        return msg

    def exigente(self):
        # O jogador exigente compra qualquer propriedade, desde que o valor do aluguel dela seja maior do que 50.
        if self.propriedade[self.posicao].aluguel > 50:
            msg = self.jogador_bo.comprar(self.jogador, self.posicao)
            return msg
        else:
            return "Falha"

    def cauteloso(self):
        # O jogador cauteloso compra qualquer propriedade desde que ele tenha uma reserva de 80 saldo sobrando
        # depois de realizada a compra.
        if (self.jogador.conta - self.propriedade[self.posicao].venda) >= 80:
            msg = self.jogador_bo.comprar(self.jogador, self.posicao)
            return msg
        else:
            "Falha"

    def aleatorio(self):
        # O jogador aleatório compra a propriedade que ele parar em cima com probabilidade de 50%.
        msg = (
            self.jogador_bo.comprar(self.jogador, self.posicao)
            if self.probabilidade_50 == 2
            else "Falha"
        )
        return msg
