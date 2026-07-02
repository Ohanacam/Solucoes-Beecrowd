class NodoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.chave,
                                    self.chave,
                                    self.direita and self.direita.chave)

class ArvoreBinaria:
    def __init__(self):
        self.inicio = None

    def ArvoreVazia(self,raiz):
        return raiz == None


    def insere(self, raiz, nodo):
        if raiz is None:
            raiz = nodo
        elif nodo.chave > raiz.chave:
            if raiz.direita is None:
                raiz.direita = nodo
            else:
                self.insere(raiz.direita, nodo)
        else:
            if raiz.esquerda is None:
                raiz.esquerda = nodo
            else:
                self.insere(raiz.esquerda, nodo)

    def pre_ordem(self, raiz):
        if raiz is not None:
          print(raiz.chave, end = ' ')
          self.pre_ordem(raiz.esquerda)
          self.pre_ordem(raiz.direita)

    def in_ordem(self, raiz):
        if raiz is not None:
          self.in_ordem(raiz.esquerda)
          print(raiz.chave, end = ' ')
          self.in_ordem(raiz.direita)

    def pos_ordem(self, raiz):
        if raiz is not None:
          self.pos_ordem(raiz.esquerda)
          self.pos_ordem(raiz.direita)
          print(raiz.chave, end = ' ')

    def procurar(self, raiz, letra_procurar ):
        if raiz is not None:
          if raiz.chave == letra_procurar:
            print(letra_procurar,"existe")
          elif letra_procurar < raiz.chave:
            self.procurar(raiz.esquerda, letra_procurar)
          else:
            self.procurar(raiz.direita, letra_procurar)
        else:
          print(letra_procurar,"nao existe")



Arvore = ArvoreBinaria()
raiz = None

while True:
    try:
        operacao = list(map(str, input().split()))
        comando = operacao[0]

        if comando == 'I':
            letra = operacao[1]
            if Arvore.ArvoreVazia(raiz):
                raiz = NodoArvore(letra)
            else:
                nodo = NodoArvore(letra)
                Arvore.insere(raiz, nodo)
        elif comando == 'PREFIXA':
            Arvore.pre_ordem(raiz)
            print()

        elif comando == 'INFIXA':
            Arvore.in_ordem(raiz)
            print()

        elif comando == 'POSFIXA':
            Arvore.pos_ordem(raiz)
            print()

        elif comando == 'P':
            letra_procurar = operacao[1]
            Arvore.procurar(raiz, letra_procurar)

    except EOFError:
        break