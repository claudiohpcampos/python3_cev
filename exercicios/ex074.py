from random import randint
num = (randint(0, 10), randint(0,10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os números escolhidos foram {num}')
print('Os números escolhidos foram ', end=' ')
for n in num:
    print(n, end=' ')
print(f'\nO maior número sorteado foi {max(num)}')
print(f'O menor número sorteado foi {min(num)}')
