from random import randint
from time import sleep

print('Oi!')
sleep(0.5)
print('Vamos brincar?')
sleep(1)
print('Sim? Ok, vou pensar em um número e você tenta adivinhar ok?')
pc = randint(0, 5)
palpites = 1
sleep(0.5)
j = int(input('Pronto! Agora tente adivinhar [de 0 a 5]: '))
while pc != j:
    palpites += 1
    if j > pc:
        ajuda = 'menos'
    if j < pc:
        ajuda = 'mais'
    j = int(input('{}...tente de novo[0 a 5]: '.format(ajuda)))
print('Isso! Você adivinhou! PARABÉNS! Você precisou de {} palpites para acertar'.format(palpites))
