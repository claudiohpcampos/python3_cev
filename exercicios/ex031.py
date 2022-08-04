km = float(input('Qual a distância da sua viagem? '))
print('Você está prestes a iniciar uma viagem de {:.0f}Km'.format(km))
if km <= 200:
    preco = km * 0.50
elif km > 200:
    preco = km * 0.45
print('E o preço da sua vigem será de R${:.2f}'.format(preco))
