nome = str(input('Digite seu nome completo: ')).strip().title()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome.split()[0]))
print('Seu último nome é {}'.format(nome.rsplit()[-1]))
