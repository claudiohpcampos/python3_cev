from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0,2)
print('\033[33m=*\033[m' * 5)
print(' \033[34mJOKENPÔ\033[m')
print('\033[33m=*\033[m' * 5)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jog = int(input('Qual a sua jogada? '))
if jog > 2:
    print('JOGADA INVÁLIDA')
    exit()
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
sleep(1)
print('Computador escolheu {}'.format(itens[comp]))
print('Jogador escolheu {}'.format(itens[jog]))
if comp == 0:
    if jog == 0:
        print('EMPATOU')
    elif jog == 1:
        print('JOGADOR VENCE')
    elif jog == 2:
        print('COMPUTADOR VENCE')
if comp == 1:
    if jog == 0:
        print('COMPUTADOR VENCE')
    elif jog == 1:
        print('EMPATOU')
    elif jog == 2:
        print('JOGADOR VENCE')
if comp == 2:
    if jog == 0:
        print('JOGADOR VENCE')
    elif jog == 1:
        print('COMPUTADOR VENCE')
    elif jog == 2:
        print('EMPATOU')
