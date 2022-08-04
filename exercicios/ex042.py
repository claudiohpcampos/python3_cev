print('\033[32m-=\033[m' * 15)
print(' \033[33mAnalisador de Triângulos 2.0\033[m')
print('\033[32m-=\033[m' * 15)
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    if s1 == s2 and s2 == s3:
        tipo = 'EQUILÁTERO'
    elif s1 != s2 and s2 != s3 and s3 != s1:
        tipo = 'ESCALENO'
    else:
        tipo = 'ISÓCELES'
    print('Os segmentos acima podem formar um \033[34mTRIÂNGULO {}\033[m.'.format(tipo))
else:
    print('Os segmentos acima \033[31mNÃO\033[m podem formar um \033[34mTRIÂNGULO\033[m.')
