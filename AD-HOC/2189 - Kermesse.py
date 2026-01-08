teste = 1
while True:
    n = int(input())
    if n == 0:
        break

    participantes = list(map(int, input().split()))
    vencedor = None

    for i, participante in enumerate(participantes, 1):
        if participante == i:
            vencedor = participante
            break

    print('Teste %d' % teste)
    teste += 1
    print(vencedor)
    print()