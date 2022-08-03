from random import randint
from time import sleep
print('\033[33m','-=' * 28, '\033[m')
print('  \033[34mVou pensar em um número entre 0 e 5. Tente adivinhar...\033[m')
print('\033[33m','-=' * 28, '\033[m')
comp = randint(0,5)
jog = int(input('Em que número pensei? '))
print('\033[34mPROCESSANDO...\033[m' )
sleep(1)
if jog < 0 or jog > 5:
    print('\033[31mNÚMERO INVÁLIDO. TENTE NOVAMENTE!!!\033[m')
elif jog == comp:
    print('\033[33mPARABÉNS ! Você conseguiu me vencer!\033[m')
elif jog != comp:
    print('\033[31mGANHEI ! Eu pensei no número {} e não no {}.\033[m'.format(comp, jog))
