codigo = int(input('digite o codigo do item'))
quantidade = int(input('digite a quantidade'))

if codigo == 1:
  total = (4.00 * quantidade)

elif codigo == 2:
  total = (4.50 * quantidade)

elif codigo == 3:
  total = (5.00 * quantidade)

elif codigo == 4:
  total = (2.00 * quantidade)

elif codigo == 5:
  total = (1.50 * quantidade)

print('Total: R$', total)