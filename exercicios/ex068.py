from random import randint
print('\033[33m=-\033[m' * 13)
print(' \033[33;44mVAMOS JOGAR PAR OU ÍMPAR\033[m')
c = 0
while True:
    comp = randint(0, 10)
    print('\033[33m=-\033[m' * 13)
    jog = int(input('Digite um valor: '))
    total = jog + comp
    opcao = ' '
    while opcao not in 'PI':
        opcao = str(input('PAR ou ÍMPAR? [P/I] ')).strip().upper()[0]
        print('\033[33m-\033[m' * 26)
    print(f'Você jogou {jog} e o computador {comp}. Total de {total}', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    print('\033[33m-\033[m' * 26)
    if opcao == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            c += 1
        else:
            print('Você PERDEU!')
            break
    elif opcao == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            c += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {c} vezes.')
