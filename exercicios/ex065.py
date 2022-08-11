opcao = 'S'
soma = quantidade = media = maior = menor = 0
while opcao in 'S':
    num = int(input('Digite um número: '))
    soma += num
    quantidade += 1
    if quantidade == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
media = soma / quantidade
print(f'Você digitou {quantidade} e a média foi {media}')
print(f'O maior valor foi {maior} e o menor {menor}')
