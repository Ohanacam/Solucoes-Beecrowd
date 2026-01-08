def filtro_entrada(total):
    sinais = []
    nomes = []
    for i in range(total):
        entrada = input()
        if entrada[0] in ('+', '-'):
            sinal = entrada[0]
            nome = entrada[1:].strip()
            sinais.append(sinal)
            nomes.append(nome)
    return sinais, nomes

def conta_sinais(sinais):
    total_positivo = 0
    total_negativo = 0
    for sinal in sinais:
      if sinal == '+':
        total_positivo += 1
      elif sinal == '-':
        total_negativo += 1
    return total_positivo, total_negativo

def ordenar(nomes):
    for i in range(len(nomes)):
        for j in range(i+1, len(nomes)):
            if nomes[i] > nomes[j]:
                nomes[i], nomes[j] = nomes[j], nomes[i]
    return nomes

total = int(input())
sinais, nomes = filtro_entrada(total)
total_positivo, total_negativo = conta_sinais(sinais)
nomes_ordenados = ordenar(nomes)

for nome in nomes_ordenados:
  print(nome)

print('Se comportaram:', total_positivo, '|', 'Nao se comportaram:', total_negativo)