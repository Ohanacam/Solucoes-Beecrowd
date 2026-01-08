quant = int(input())
lista = {}

for i in range(quant):
    num = int(input())
    if num in lista:
        lista[num] += 1
    else:
        lista[num] = 1

for x in lista:
    print("%d aparece %d vez(es)" % (x, lista[x]))