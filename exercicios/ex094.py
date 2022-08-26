cadastro = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).strip().title()
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    cadastro.append(pessoa.copy())
    while True:
        opc = str(input('Quer continuar? [S/N] ')).strip().upper()
        if opc in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if opc == 'N':
        break
print('-=' * 30)
print(f'Ao todo temos {len(cadastro)} pessoas cadastradas.')
media = soma / len(cadastro)
print(f'A média de idade é de {media:.2f} anos')
print('As mulheres cadastradas foram: ', end='')
for p in cadastro:
    if p['sexo'] in 'F':
        print(f'{p["nome"]}', end=' ')
print()
print('Lista das pessoas que estão acima da média:')
print()
for p in cadastro:
    if p['idade'] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< FIM >>')
