jogador = dict()
dados = list()
jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
quant = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, quant):
    dados.append(int(input(f'  Quantos gols na partida {c+1}? ')))
jogador['gols'] = dados
jogador['total'] = sum(dados)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'  => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols')
print('-=' * 30)
