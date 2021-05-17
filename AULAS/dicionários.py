dados = list()
dados.append('Pedro')
dados.append(25)
dados = {'nome': 'Pedro', 'idade': 25}
dados['sexo'] = 'M'
del dados['idade']
filme = {'titulo': 'Star Wars',
         'ano': 1977, 'diretor': 'George Lucas'}
filme1 = {'titulo': 'Avengers', 'ano': 2012, 'diretor': 'Joss Whedon'}
filme2 = {'titulo': 'Matrix', 'ano': 1999, 'diretor': 'Wachowski'}
locadora = []
locadora.append(filme)
locadora.append(filme1)
locadora.append(filme2)
for f in locadora:
    for k, v in f.items():
        print(f'O {k} é {v} ')
    print('-' * 30)
