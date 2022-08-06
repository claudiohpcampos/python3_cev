media = 0
velhoh = 0
nomevelho = ''
contm = 0
for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M / F]: ')).strip()
    media += idade
    if p == 1 and sexo in 'Mm':
        velhoh = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > velhoh:
        velhoh = idade
        nomevelho = nome
    if idade < 20 and sexo in 'Ff':
        contm += 1
print('A média de idade do grupo é {:.0f} anos.'.format(media / 2))
print('O homem mais velho tem {} anos e se chama {}.'.format(velhoh, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(contm))
