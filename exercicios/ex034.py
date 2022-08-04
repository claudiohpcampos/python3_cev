atual = float(input('Qual é o salário do funcionário? R$'))
if atual <= 1250:
    salario = atual + (atual * 15 / 100)
else:
    salario = atual + (atual * 10 / 100)
print('Quem ganhava R${:.2f} passa a receber R${:.2f} agora.'.format(atual, salario))