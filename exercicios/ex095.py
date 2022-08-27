jogador = dict()
partidas = list()
time = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
    quant = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, quant):
        partidas.append(int(input(f'  Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        opc = str(input('Quer continuar? [S/N] ')).strip().upper()
        if opc in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if opc == 'N':
        break
print('-' * 60)
print('Cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 60)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 60)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 encerrar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f'  -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'  => No jogo {i+1}, fez {g} gols.')
    print('-' * 60)
print('<< VOLTE SEMPRE! >>')
