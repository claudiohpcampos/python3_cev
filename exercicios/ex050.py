soma = 0
cont = 0
for n in range(1, 7):
    num = int(input('Digite o {}º valor: '.format(n)))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('Você informou {} números e a soma foi {}'.format(cont, soma))
