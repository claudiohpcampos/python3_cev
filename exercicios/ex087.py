matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
parsoma = 0
colter = 0 # soma da terceira coluna
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print('=-' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end=' ')
        if matriz[linha][coluna] % 2 == 0:
            parsoma += matriz[linha][coluna]
    print()
print('=-' * 30)

print(f'A soma dos valores pares é {parsoma}')
for linha in range(0, 3):
    colter += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é {colter}')
maior = matriz[1][0]
if matriz[1][1] > maior:
    maior = matriz[1][1]
if matriz[1][2] > maior:
    maior = matriz[1][2]
print(f'O maior valor da segunda linha é {maior}')
