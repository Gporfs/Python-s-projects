from time import sleep
from random import randint

i = randint(0, 2)
if i == 0:
    pc = 'p'
elif i == 1:
    pc = 'pa'
elif i == 2:
    pc = 't'
print('Olá!')
sleep(1)
print('Vamos jogar jokenpô?')
sleep(1)
print('Sim?')
sleep(1)
print('OK')
sleep(1)
print('JO...')
sleep(1)
print('KEN...')
sleep(1)
print('PÔÔ!!!')
sleep(1)
j = str(input('''JOGADAS POSSIVEIS:
[P]para pedra
[PA]para papel
[T]para tesoura
Sua jogada é: ''')).strip().lower()
if j == 'pedra':
    j = 'p'
elif j == 'papel':
    j = 'pa'
elif j == 'tesoura':
    j = 't'
if j == 'p' and pc == 't' or j == 'pa' and pc == 'p' or j == 't' and pc == 'pa':
    print('VOCÊ GANHOU!!!')
elif j == pc:
    print('EMPATE!!!')
elif pc == 'p' and j == 't' or pc == 'pa' and j == 'p' or pc == 't' and j == 'pa':
    print('VOCÊ PERDEU!!!')
if pc == 'p':
    pc = 'pedra'
elif pc == 'pa':
    pc = 'papel'
elif pc == 't':
    pc = 'tesoura'
print('O computador jogou {}'.format(pc.upper()))
