salario = float(input('digite a quantidade'))

if (salario <= 0) or (salario >= 400.00):
  indice = 15
  perce_reajuste = (salario*0.15)
  salario_novo = (perce_reajuste + salario)

elif (salario <= 400.01) or (salario >= 800.00):
  indice = 12
  perce_reajuste = (salario*0.12)
  salario_novo = (perce_reajuste + salario)

elif (salario <= 800.01) or (salario >= 1200.00):
  indice = 10
  perce_reajuste = (salario*0.10)
  salario_novo = (perce_reajuste + salario)

elif (salario <= 1200.01) or (salario >= 2000.00):
  indice = 7
  perce_reajuste = (salario*0.07)
  salario_novo = (perce_reajuste + salario)

elif (salario >= 2000.01):
  indice = 4
  perce_reajuste = (salario*0.04)
  salario_novo = (perce_reajuste + salario)

print(f'seu novo salario:{salario_novo}')
print(f'O reajuste ganho {perce_reajuste}')
print(f'nem percentual:{indice}%')