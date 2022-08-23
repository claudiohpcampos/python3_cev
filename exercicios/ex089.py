boletim = []
while True:
    nome = str(input('Nome: ')).strip().title()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    boletim.append([nome, [n1, n2], media])
    opc = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if opc in 'N':
        break
print('-=' * 15)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 30)
for i, a in enumerate(boletim):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 30)
    opc2 = int(input('Mostrar as notas de qual aluno? (999 para encerrar): '))
    if opc2 == 999:
        print('FINALIZANDO...')
        break
    if opc2 <= len(boletim) -1:
        print(f'Notas de {boletim[opc2][0]} são {boletim[opc2][1]}')
print('<<< VOLTE SEMPRE! >>>')
