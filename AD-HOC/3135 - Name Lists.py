tam = []
nomes = []
vetor_atual = [0] * 20
vetores = [vetor_atual]

num_nomes = int(input())
for i in range(num_nomes):
    nome = input()
    nomes.append(nome)

for nome_item in nomes:
    tam.append(len(nome_item))

for i in range(len(nomes)):
    comprimento = tam[i]

    for j in range(len(vetores)):
        if vetores[j][comprimento] == 0:
            vetores[j][comprimento] = nomes[i]
            break
    else:
        novo_vetor = [0] * 20
        novo_vetor[comprimento] = nomes[i]
        vetores.append(novo_vetor)

for vetor in vetores:
    elementos = []
    for elemento in vetor:
        if elemento != 0:
            elementos.append(elemento)
    elementos_formatados = ', '.join(elementos)
    print(elementos_formatados)