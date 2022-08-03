nome = str(input('Digite uma frase: ')).strip()
print('A letra A aparece {} vezes na frase.'.format((nome.upper()).count('A')))
print('A primeira letra a apareceu na posição {}'.format((nome.upper()).find('A') + 1))
print('A última letra A aparece na posição {}'.format((nome.upper()).rfind('A') + 1))
