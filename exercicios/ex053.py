print('-=' * 12)
print(' DETECTOR DE PALÍNDROMO')
print('-=' * 12)
frase = str(input('Digite uma frase: ')).strip().upper().split()
junto = (''.join(frase))
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
