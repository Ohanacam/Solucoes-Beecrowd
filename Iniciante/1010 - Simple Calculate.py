cod, n, val = map(float, input().split())
cod2, n2, val2 = map(float, input().split())

cal = n*val
cal2 = n2*val2

sum = cal + cal2

print('VALOR A PAGAR: R$ %.2f'%sum)