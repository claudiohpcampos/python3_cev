cont = soma = num = 0
num = int(input('Digite um número [999 para encerrar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para encerrar]: '))
print(f'Você digitou {cont} números e a soma entre eles foi {soma}.')
