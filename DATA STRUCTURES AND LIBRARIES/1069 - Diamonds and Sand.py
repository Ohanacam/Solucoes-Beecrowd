class ClassePilha:
    def __init__(self):
        self.TOPO = -1
        self.Pilha = []

    def PilhaVazia(self):
        return self.TOPO == -1

    def PUSH(self, Valor):
        self.TOPO = self.TOPO + 1
        self.Pilha.append(Valor)

    def POP(self):
        if self.PilhaVazia():
            return None
        else:
            Valor = self.Pilha.pop()
            self.TOPO = self.TOPO - 1
            return Valor

def verifica_diamantes(expressao):
    pilha = ClassePilha()
    diamantes = 0

    for i in expressao:
        if i == '<':
            pilha.PUSH(i)
        elif i == '>':
            if not pilha.PilhaVazia() and pilha.POP() == '<':
                diamantes += 1

    return diamantes


num = int(input())
expressions = []
        
for i in range(num):
    expressao = input()
    expressions.append(expressao)
        
for expressao in expressions:
    quantidade_diamantes = verifica_diamantes(expressao)
    print(quantidade_diamantes)