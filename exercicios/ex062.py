print('\033[33m-=\033[m' * 9)
print('\033[34mGerador de PA 3.0')
print('\033[33m-=\033[m' * 9)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
opcao = 10
while opcao != 0:
    total = total + opcao
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo = termo + razao
        cont += 1
    print('PAUSA')
    opcao = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados')
