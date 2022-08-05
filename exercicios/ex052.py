cont = 0
print('==== NÚMEROS PRIMOS =====')
num = int(input('Digite um número: '))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', c, '\033[m', end=' ')
        cont += 1
    else:
        print('\033[31m', c, '\033[m', end=' ')
print('\nO número {} foi divisível {} vezes.'.format(num, cont))
if cont == 2:
    print('E por isso ele \033[33mÉ PRIMO!\033[m')
else:
    print('E por isso ele \033[31mNÃO É PRIMO!\033[m')
