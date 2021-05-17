def ficha(n='', g='0'):
    if n.strip() == '':
        n = '<desconhecido>'
    if g.isnumeric():
        g = int(g)
    else:
        g = 0
    return f'O jogador {n} marcou {g} gol(s) no campeonato.'


nome = str(input('Nome: '))
marcados = str(input('Gol(s): '))
print(ficha(nome, marcados))
