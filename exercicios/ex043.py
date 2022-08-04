print('\033[33m-=\033[m' * 9)
print(' Calculadora IMC')
print('\033[33m-=\033[m' * 9)
p = float(input('Qual é o seu peso? (Kg) '))
a = float(input('Qual é a sua altura? (m) '))
imc = p / (a ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está \033[31mABAIXO DO PESO\033[m')
elif imc <= 25:
    print('Parabéns, você está na faixa de peso \033[32mNORMAL\033[m')
elif imc <= 30:
    print('Você está com \033[33mSOBREPESO\033[m')
elif imc <= 40:
    print('Você está na faixa de \033[31mOBESIDADE\033[m')
else:
    print('\033[31mCUIDADO\033[m, Você está na faixa de \033[0;30;41mOBESIDADE MÓRBIDA\033[m')
