lista = []
lpar = []
limpar = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        lpar.append(n)
    elif n % 2 == 1:
        limpar.append(n)
    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao in 'N':
        break
print(f'A lista completa é: {lista}')
print(f'A lista de pares é: {lpar}')
print(f'A lista de ímpares é: {limpar}')
