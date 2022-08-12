print('\033[31mTABUADA 3.0\033[m')
while True:
    n = int(input('Quer ver a tabuada de qual número? '))
    print('-' * 35)
    if n <= 0:
        break
    cont = 0
    while cont != 10:
        cont += 1
        print(f'{n} x {cont} = {n * cont}')
    print('-' * 35)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
