listnum = []
listpar = []
listimpar = []
for c in range(0, 7):
    num = int(input(f'Digite o {c + 1}º valor: '))
    if num % 2 == 0:
        listpar.append(num)
    elif num % 2 == 1:
        listimpar.append(num)
listpar.sort()
print(f'Os valores pares digitados foram: {listpar}')
listimpar.sort()
print(f'Os valores ímpares digitados foram: {listimpar}')
listnum.append(listpar)
listnum.append(listimpar)
print(listnum)
