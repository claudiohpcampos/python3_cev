num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
  'treze', 'catorze', 'quinze', 'desesseis', 'desessete',
   'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        print(f'Você digitou o número {num[n]}')
    else:
        print('Tente novamente. ', end='')
    op = ' '
    if op not in 'SN':
        op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if op == 'N':
            break
print('---  FIM DO PROGRAMA ---')
