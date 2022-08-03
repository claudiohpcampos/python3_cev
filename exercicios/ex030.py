num = int(input('Me diga qualquer número: '))
if num % 2 == 0:
    print('O número {} é \033[34mPAR\033[m'.format(num))
else:
    print('O número {} é \033[34mÍMPAR\033[m'.format(num))
