casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
ano = int(input('Quantos anos de financiamento? '))
prestacao = casa / (ano * 12)
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(casa, ano, prestacao))
if prestacao <= salario * 30 /100:
    print('Empréstimo pode ser \033[32mCONCEDIDO!\033[m')
else:
    print('Empréstimo \033[31mNEGADO!\033[m')
