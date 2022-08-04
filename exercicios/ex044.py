preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Qual é a sua opção? '))
if opcao == 1:
    valor = preco - (preco * 10 / 100)
elif opcao == 2:
    valor = preco - (preco * 5 / 100)
elif opcao == 3:
    valor = preco
    print('Sua compra será parcelada em 2x sem juros de R${:.2f}'.format(preco / 2))
elif opcao ==4:
    parc = int(input('Quantas parcelas? '))
    valor = preco + (preco *20 / 100)
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parc, valor / parc))
else:
    print('OPÇÃO INVÁLIDA')
    preco = 0
    valor = 0
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, valor))
