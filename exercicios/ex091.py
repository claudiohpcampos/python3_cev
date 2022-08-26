from random import randint
from time import sleep
from operator import itemgetter
aposta = {'jogador 1': randint(1, 6), 'jogador 2': randint(1, 6), 'jogador 3': randint(1, 6), 'jogador 4': randint(1, 6)}
ranking = dict()
print('Valores sorteados:')
print('-=' * 30)
for k, v in aposta.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print('-=' * 30)
print('\t== RANKING DOS JOGADORES ==')
ranking = sorted(aposta.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'\t{i+1}º lugar: {v[0]} com {v[1]} pontos.')
    sleep(1)
print('-=' * 30)
