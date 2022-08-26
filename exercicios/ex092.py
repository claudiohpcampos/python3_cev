from datetime import datetime
pessoa = dict()
pessoa['nome'] = str(input('Nome: ')).strip().title()
nasc = int(input('Ano de Nascimento: '))
pessoa['idade'] = datetime.now().year - nasc
pessoa['ctps'] = int(input('Carteia de Trabalho (0 não tem): '))
if pessoa['ctps'] != 0:
    pessoa['contratacao'] = int(input('Ano de Contratação: '))
    pessoa['salario'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = (pessoa['contratacao'] - nasc + 35)
print('-=' * 30)
for k, v in pessoa.items():
    print(f'\t- {k} tem o valor {v}')
