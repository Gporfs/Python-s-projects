lista = list()
dados = []
while True:
    dados.append(str(input('NOME: ')).capitalize())
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    media = (dados[1] + dados[2]) / 2
    dados.append(media)
    lista.append(dados[:])
    dados.clear()
    r = str(input('Deseja continuar? [S/N] '))
    if r in 'Nn':
        break
print('=-'*30)
print(f'{"N°":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*30)
for p in range(0, len(lista)):
    print(f'{p:<4}{lista[p][0]:<10}{lista[p][3]:>8.1f}')
print('=-'*30)
while True:
    aluno = int(input('Deseja as notas de qual aluno?(999 interrompe) '))
    if aluno == 999:
        break
    print(f'As notas de {lista[aluno][0]} são: ')
    print(f'nota 1: {lista[aluno][1]}')
    print(f'nota 2: {lista[aluno][2]}')
print('FINALIZANDO...')
print('<<<< VOLTE SEMPRE >>>>')
