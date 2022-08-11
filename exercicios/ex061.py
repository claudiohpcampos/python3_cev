print('Gerador de PA 2.0')
print('-=' * 9)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo = termo + razao
    cont += 1
print('FIM')
