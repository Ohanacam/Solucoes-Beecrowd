n= input().split()
lista = []
i = 0
while(int(n[i])!=0):
    lista.append(int(n[i]))
    i += 1
print(max(lista))