jogador = dict()
jogador['Nome'] = str(input('Nome: '))
jogador['Partidas'] = int(input(f'Número de partidas jogadas por {jogador["Nome"]}: '))
jogador['gols'] = list()
jogador['total'] = 0
for c in range(0, jogador['Partidas']):
    gols = int(input(f'Gols Marcados na partida {c + 1}: '))
    jogador['gols'].append(gols)
    jogador['total'] += gols
print('-='*30)
print(f'O jogador {jogador["Nome"]} jogou {jogador["Partidas"]} partidas')
for p, g in enumerate(jogador['gols']):
    print(f'  =>Na partida {p+1} marcou {g} gols')
print(f'Foi um total de {jogador["total"]} gols')
