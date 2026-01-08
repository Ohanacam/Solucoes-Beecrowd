while 1:
	quant = int(input())

	if (quant == 0):
		break

	resultados = list(map(int,input().split()))
	mary = 0
	john = 0
	for x in resultados:
		if(x == 0):
			mary += 1
		else:
			john += 1
	print("Mary won %d times and John won %d times" %(mary,john))