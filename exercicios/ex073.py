time = ('Palmeiras', 'Corinthians', 'Fluminense', 'Athlético-PR', 'Flamengo',
 'Atlético-MG', 'Internacional', 'Bragantino', 'Santos', 'América-MG', 'São Paulo',
  'Botafogo', 'Goiás', 'Ceará-SC', 'Fortaleza', 'Cuiabá',
   'Avaí', 'Coritiba', 'Atlético-GO', 'Juventude')
print(f'Os cinco primeiros colocados na tabela: {time[:5]}')
print(f'Os quatro últimos colocados na tabela: {time[-4:]}')
print(f'Os times da tabela em ordem alfabética: {sorted(time)}')
print(f'O Flamengo está na {time.index("Flamengo") + 1}ª posição')
