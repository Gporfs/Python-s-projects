aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'aprovado'
elif 7 > aluno['media'] > 5:
    aluno['situação'] = 'recuperação'
else:
    aluno['situação'] = 'reprovado'
for k, v in aluno.items():
    print(f'{k} é {v}')
