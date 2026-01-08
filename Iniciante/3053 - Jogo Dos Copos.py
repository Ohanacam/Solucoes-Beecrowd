num = int(input()) 
posicao = input()
copoA = False 
copoB = False 
copoC = False 

if posicao == "A":
    copoA = True

elif posicao == "B":
    copoB = True

elif posicao == "C":
    copoC = True


for i in range(num):
    mov = int(input())

    if mov == 1:
        if copoA == True:
            copoA = False
            copoB = True
        elif copoB == True:
            copoB = False
            copoA = True
    
    if mov == 2:
        if copoB == True:
            copoB = False
            copoC = True
        elif copoC == True:
            copoC = False
            copoB = True

    if mov == 3:
        if copoA == True:
            copoA = False
            copoC = True
        elif copoC == True:
            copoC = False
            copoA = True

if copoA == True:
    print("A")

elif copoB == True:
    print("B")

elif copoC == True:
    print("C")