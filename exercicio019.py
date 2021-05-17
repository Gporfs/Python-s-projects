from datetime import datetime

now = datetime.now()
a = now.year
ano = int(input('Digite o seu ano de nascimento: '))
i = a - ano
if i <= 9:
    print('Este atleta é classe: MIRIM!')
elif i <= 14:
    print('Este atleta é classe: INFANTIL!')
elif i <= 19:
    print('Este atleta é classe: JUNIOR!')
elif i < 25:
    print('Este atleta é classe: SÊNIOR!')
elif i > 25:
    print('Este atleta é classe: MASTER!')
