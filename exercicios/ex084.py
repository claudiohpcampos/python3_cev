lista = []
dados = []
cont = maior = menor = 0
while True:
    dados.append(str(input('Nome: ')).strip().title())
    dados.append(int(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    lista.append(dados[:])
    dados.clear()
    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao in 'N':
        break
print(f'A lista completa: {lista}')
for p in lista:
    cont += 1
print(f'Foram cadastradas {cont} pessoas.') # pode usar len(lista)
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ',end='')
for p in lista:
    if p[1] == menor:
        print(f'{p[0]} ', end='')
print()
