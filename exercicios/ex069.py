contidade = contM = contF = 0
while True:
    print('-' * 24)
    print(f'{"CADASTRE UMA PESSOA": ^24}')
    print('-' * 24)
    idade = int(input('Idade: '))
    if idade > 18:
        contidade += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if sexo == 'M':
            contM += 1
        if sexo == 'F' and idade < 20:
            contF += 1
    print('-' * 24)
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if opcao == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {contidade}.')
print(f'Ao tdo temos {contM} homens cadastrados')
print(f'E temos {contF} mulheres com menos de 20 anos')
