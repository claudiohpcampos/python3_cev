from random import randint
comp = randint(0, 10)
cont = 0
print('Sou seu computador...')
print('Acabei de pensar em um número de 0 a 10.')
print('Será que você consegue adivinhar qual foi?')
while True:
    jog = int(input('Qual é seu palpite? '))
    cont += 1
    if jog > comp:
        print('Menos... Tente mais uma vez.')
    if jog < comp:
        print('Mais... Tente mais uma vez.')
    elif jog == comp:
        break
print(f'Acertou com {cont} tentativas. Parabéns !')
