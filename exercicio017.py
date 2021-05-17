from datetime import datetime
now = datetime.now()
ano = now.year
print('\033[32m=-='*20)
print('ALISTAMENTO MILITAR')
print('=-='*20)
i = int(input('\033[mDigite seu ano de nascimento: '))
id = ano - i
if id < 18:
    print('Ainda vai se alistar, faltam {} anos'.format(18 - id))
elif id > 18:
    print('Já passou da hora de se alistar, já passou {} anos do prazo'.format(id-18))
elif id == 18:
    print('Está na hora de se alistar')
