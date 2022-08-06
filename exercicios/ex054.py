from datetime import date
ano = date.today().year
cont = 0
cont1 = 0
for n in range(1, 8):
    nasc = int(input('em que ano a {}ª pessoa nasceu? '.format(n)))
    if ano - nasc <= 21:
        cont += 1
    else:
        cont1 += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(cont1))
print('E também tivemos {} pessoas menores de idade'.format(cont))