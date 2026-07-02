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
          print(raiz.chave, end=' ')
          self.pre_ordem(raiz.esquerda)
          self.pre_ordem(raiz.direita)

    def in_ordem(self, raiz):
        if raiz is not None:
          self.in_ordem(raiz.esquerda)
          print(raiz.chave, end=' ')
          self.in_ordem(raiz.direita)

    def pos_ordem(self, raiz):
        if raiz is not None:
          self.pos_ordem(raiz.esquerda)
          self.pos_ordem(raiz.direita)
          print(raiz.chave, end=' ')


    def teste(self, raiz):
      for i in range(vezes):
        if Arvore.ArvoreVazia(raiz):
          raiz = NodoArvore(valores[i])

        else:
          nodo = NodoArvore(valores[i])
          Arvore.insere(raiz, nodo)

      print('Pre.:', end="")
      Arvore.pre_ordem(raiz)
      print('\nIn..:', end="")
      Arvore.in_ordem(raiz)
      print('\nPost: ', end="")
      Arvore.pos_ordem(raiz)
      print()



Arvore = ArvoreBinaria()
raiz = None
cont = 1
casos = int(input())
while True:
  for i in range(casos):
   vezes = int(input())
   valores = list(map(int, input().split()))
   print('Case', cont, ':')
   cont += 1
   Arvore.teste(raiz)
   print()