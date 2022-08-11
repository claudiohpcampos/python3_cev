from time import sleep
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
while True:    
    print('''[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa''')    
    opcao = int(input('>>>>> Qual sua opção? '))
    if opcao < 0 or opcao > 5:
        print('Opção inválida. Tente novamente')
    if opcao == 1:
        print(f'O resultado de {num1} + {num2} = {num1 + num2}')
    if opcao == 2:
        print(f'O resultado de {num1} x {num2} = {num1 * num2}')
    if opcao == 3:
        maior = ' '
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print(f'Entre {num1} e {num2}, o maior é {maior}')
    if opcao == 4:
        print('Informe os números novamente:')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    print('=-=' * 10)
    if opcao == 5:
        break
print('Finalizando...')
print('=-=' * 10)
sleep(1)
print('Fim do programa! Volte sempre!')
