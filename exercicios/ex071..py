print('=' * 30)
print(f'{"BANCO EVIL CORP": ^30}')
print('=' * 30)
saque = int(input('Que valor você quer sacar? R$ '))
total = saque
cedula = 50
totced = 0
while True:
    if total >= cedula:
        total -= cedula
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totced = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO EVIL CORP! Tenha um bom dia!')
