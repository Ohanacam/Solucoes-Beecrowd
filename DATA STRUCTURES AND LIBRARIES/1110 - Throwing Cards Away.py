class ClasseFila:
    def __init__(self):
        self.tam = 51
        self.Fila = [0] * self.tam
        self.INI = -1
        self.FIM = -1

    def FilaVazia(self):
        return self.INI == -1 and self.FIM == -1

    def FilaCheia(self):
        if self.INI == 0 and self.FIM == self.tam - 1:
            return True
        elif self.FIM + 1 == self.INI:
            return True

    def QUEUE(self, Valor):
            if self.FilaVazia():
                self.INI = 0
                self.FIM = 0
            else:
                if self.FIM == self.tam - 1:
                    self.FIM = 0
                else:
                    self.FIM += 1
            self.Fila[self.FIM] = Valor
            return Valor

    def DEQUEUE(self):
            Valor = self.Fila[self.INI]
            if self.INI == self.FIM:
                self.INI = -1
                self.FIM = -1
            elif self.INI == self.tam - 1:
                self.INI = 0
            else:
                self.INI += 1
            return Valor

    def organiza_cartas(self, n):
        for i in range(1, n + 1):
            self.QUEUE(i)
        discarded_cards = ClasseFila()
        while self.INI != self.FIM:
            discarded_card = self.DEQUEUE()
            discarded_cards.QUEUE(discarded_card)
            self.QUEUE(self.DEQUEUE())
        return discarded_cards, self.Fila[self.INI]

while True:
    n = int(input())
    if n == 0:
        break
    deck = ClasseFila()

    discarded_cards, remaining_card = deck.organiza_cartas(n)
    print("Discarded cards:", end=' ')
    while not discarded_cards.FilaVazia():
        print(discarded_cards.DEQUEUE(), end='')
        if not discarded_cards.FilaVazia():
            print(', ', end='')
    print()
    print("Remaining card:", remaining_card, end='')
    print()