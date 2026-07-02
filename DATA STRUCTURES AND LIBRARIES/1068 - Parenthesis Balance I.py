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

def verifica_parenteses(expressao):
    pilha = ClassePilha()

    for i in expressao:
        if i == '(':
            pilha.PUSH(i)
        elif i == ')':
            if not pilha.PilhaVazia() and pilha.POP() == '(':
                continue
            else:
                return "incorrect"

    if pilha.PilhaVazia():
        return "correct"
    else:
        return "incorrect"

while True:
    try:
        expressao = input()
        resultado = verifica_parenteses(expressao)
        print(resultado)
    except EOFError:
        break