media = 0
pessoa = dict()
grupo = list()
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['idade'] = int(input('Idade: '))
    media += pessoa['idade']
    pessoa['sexo'] = str(input('Sexo [M/F]: '))
    while pessoa['sexo'] not in 'MmFf':
        pessoa['sexo'] = str(input('Erro! Digite apenas [M/F]: '))
    grupo.append(pessoa.copy())
    pessoa.clear()
    r = str(input('Continuar? [S/N]: '))
    while r not in 'SsNn':
        r = str(input('Erro! Digite apenas [S/N]: '))
    if r in 'Nn':
        break
media = media / len(grupo)
print('-' * 50)
print(f'O grupo tem {len(grupo)} pessoas')
print(f'A média de idade do grupo é {media:.2f} anos')
print('As mulheres cadastradas foram: ', end='')
for p in grupo:
    if p['sexo'] in 'fF':
        print(f'[ {p["nome"]} ]', end=' ')
print()
print('Pessoas acima da média:')
for p in grupo:
    if p['idade'] > media:
        print(f'nome = {p["nome"]}, idade = {p["idade"]}, sexo = {p["sexo"]}')
print('<<<< ENCERRADO >>>>')
