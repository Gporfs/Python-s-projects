from datetime import date
ano = date.today().year
s = 0
for c in range (0,7):
    nasc = int(input('Digite seu ano de nascimento: '))
    if ano - nasc >= 18:
        r = 1
    else:
        r = 0
    s = s + r
if s == 1:
    verbo = 'é'
else:
    verbo = 'são'
if 7 - s == 1:
    verbo2 = 'é'
else:
    verbo2 = 'são'
print('{} das 7 pessoas em questão {} maiores de 18 anos enquanto {} ainda não {}'.format(s, verbo, 7-s, verbo2))