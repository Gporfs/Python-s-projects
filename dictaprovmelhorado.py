jogadores = list()
while True:
    total = 0
    jogador = dict()
    jogador['Nome'] = str(input('Nome: '))
    jogador['Partidas'] = int(input(f'Número de partidas jogadas por {jogador["Nome"]}: '))
    jogador['gols'] = list()
    jogador['total'] = 0
    for c in range(0, jogador['Partidas']):
        gols = int(input(f'Gols Marcados na partida {c + 1}: '))
        jogador['gols'].append(gols)
        total += gols
    jogador['total'] = total
    jogadores.append(jogador.copy())
    jogador.clear()
    r = str(input('Continua? [S/N]: '))
    if r in 'Nn':
        break
print('-=' * 30)
print(f'{"Cod":<4} ', end='')
cont = 0
for i in jogadores[cont]:
    print(f'{i:<15}', end='')
    cont += 1
print()
print('-' * 60)
for p, j in enumerate(jogadores):
    print(f'{p:<4} ', end='')
    for d in j.values():
        print(f'{str(d):<15}', end=' ')
    print()
print('-' * 60)
while True:
    opc = int(input('Mostrar dados de qual jogador? (999 para finalizar): '))
    if opc == 999:
        break
    if opc >= len(jogadores):
        print('Código inválido tente novamente!')
    else:
        print(f'Levantando dados do jogador {jogadores[opc]["Nome"]}...')
        for n in range(1, len(jogadores[opc]["gols"]) + 1):
            print(f'Jogo {n}: {jogadores[opc]["gols"][n - 1]} gols')
    print('=-' * 30)
print('<<<< VOLTE SEMPRE >>>>')
