c = float(input('Informe a temperatura em °C: '))
print('A temperatura de {}{:.1f}{}°C corresponde a {}{:.1f}{}°F.'.format('\033[34m', c, '\033[m', '\033[31m', ((9 * c) / 5) + 32, '\033[m'))
