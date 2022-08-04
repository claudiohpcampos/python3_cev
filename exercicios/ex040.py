n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, media))
if media < 5:
    print('O aluno está \033[31mREPROVADO\033[m.')
elif media < 7:
    print('O aluno está em \033[33mRECUPERAÇÃO\033[m.')
else:
    print('O aluno está \033[32mAPROVADO\033[m.')
