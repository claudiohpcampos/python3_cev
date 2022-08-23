from random import randint
from time import sleep
bilhete = list()
jogos = list()
print('-' * 40)
print(f'{"JOGO DA MEGA SENA":^40}')
print('-' * 40)
quant = int(input('Quantos jogos serão sorteados: '))
tot = 1
print(('-=' * 3), f' SORTEANDO {(quant)} JOGOS', ('-=' * 3))
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in bilhete:
            bilhete.append(num)
            cont += 1
        if cont >= 6:
            break
    bilhete.sort()
    jogos.append(bilhete[:])
    bilhete.clear()
    tot += 1
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print(('=-' * 10), f' < BOA SORTE! >', ('-=' * 10))
