from random import randint
from time import sleep
from operator import itemgetter
ranking = {}
jogador = {}
for num in range(1, 5):
    jogador[f'jogador{num}'] = randint(1, 6)
print('Valores Sorteados:')
for k, v in jogador.items():
    sleep(1)
    print(f'O {k} tirou o número {v}')
print('-='*30)
print('Ranking dos jogadores: ')
ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}°lugar: {v[0]} com {v[1]}')
    sleep(1)
