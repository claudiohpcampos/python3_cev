print('-=' * 13)
print(f'{"LOJA SUPER BARATÃO": ^26}')
print('-=' * 13)
soma = maiorpreco = menorpreco = cont = 0
menorprod = ' '
while True:
    prod = str(input('Nome do produto: ')).strip().lower()
    preco = float(input('Preço: R$ '))
    cont += 1
    soma += preco
    if preco > 1000:
        maiorpreco += 1  
    if cont == 1:
        menorpreco = preco
        menorprod = prod
        if preco < menorpreco:
            menorpreco = preco
            menorprod = prod
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print(f'{" FIM DO PROGRAMA ":-^26}')
print(f'O total de compras foi R${soma:.2f}')
print(f'Temos {maiorpreco} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {menorprod} e custa R${menorpreco:.2f}')
