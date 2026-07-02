class ClasseFila:
    def __init__(self):
        self.INI = -1
        self.FIM = -1
        self.tam = 1001
        self.Fila = [0] * self.tam

    def FilaCheia(self):
        if self.INI == 0 and self.FIM == 1001 - 1:
            return True
        elif self.FIM + 1 == self.INI:
            return True

    def FilaVazia(self):
        return self.INI == -1 and self.FIM == -1


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

    def organizar_avioes(self, avioes):
        L = ClasseFila()
        N = ClasseFila()
        S = ClasseFila()
        O = ClasseFila()

        while not avioes.FilaVazia():
            aviao = avioes.DEQUEUE()
            nome, cord = aviao
            if cord == -4:
                L.QUEUE(nome)
            elif cord == -3:
                N.QUEUE(nome)
            elif cord == -2:
                S.QUEUE(nome)
            elif cord == -1:
                O.QUEUE(nome)

        ordem_pouso = ClasseFila()

        while not (L.FilaVazia() and N.FilaVazia() and S.FilaVazia() and O.FilaVazia()):
            if not O.FilaVazia():
                ordem_pouso.QUEUE(O.DEQUEUE())
            if not N.FilaVazia():
                ordem_pouso.QUEUE(N.DEQUEUE())
            if not S.FilaVazia():
                ordem_pouso.QUEUE(S.DEQUEUE())
            if not L.FilaVazia():
                ordem_pouso.QUEUE(L.DEQUEUE())

        return ordem_pouso

avioes = ClasseFila()
while True:
    p = input()
    if p == '0':
        break

    if p[0] == '-':
        aux_cord = int(p)
    elif p[0] == 'A':
        avioes.QUEUE((p, aux_cord))

OrdemDePouso = avioes.organizar_avioes(avioes)
while not OrdemDePouso.FilaVazia():
    saida = OrdemDePouso.DEQUEUE()
    if OrdemDePouso.FilaVazia():
        print(saida, end='')
    else:
        print(saida, end=' ')
print()