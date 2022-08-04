print('\033[34m', '-=' * 12, '\033[m')
print(' Analisador de triângulos')
print('\033[34m', '-=' * 12, '\033[m')
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos acima \033[34mPODEM FORMAR TRIÂNGULO!\033[m')
else:
    print('OS segmentos acima \033[34mNÃO FORMAM UM TRIÂNGULO!\033[m')
