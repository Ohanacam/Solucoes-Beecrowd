pares = []
impares = []

for i in range(15):
    num = int(input())
    if num % 2 == 0:
        pares.append(num)
        if len(pares) == 5:
            for x in range(len(pares)):
                print("par[%d] = %d" % (x, pares[x]))
            pares = []

    if num % 2 != 0:
        impares.append(num)
        if len(impares) == 5:
            for x in range(len(impares)):
                print("impar[%d] = %d" % (x, impares[x]))
            impares = []

for x in range(len(impares)):
    print("impar[%d] = %d" % (x, impares[x]))

for x in range(len(pares)):
    print("par[%d] = %d" % (x, pares[x]))
