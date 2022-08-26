aluno = {}
aluno['nome'] = str(input('Nome: ')).strip().title()
aluno['media'] = float(input('Média: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif aluno['media'] >= 5:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
print('-=' * 30)
print(aluno)
print('-=' * 30)
print(f'\tNome é igual a {aluno["nome"]}')
print(f'\tMédia é igual a {aluno["media"]}')
print(f'\tSituação é igual a {aluno["situacao"]}')
