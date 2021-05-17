exp = str(input('Digite sua expressão: '))
parenteses = []
for simb in exp:
    if simb == '(':
        parenteses.append('(')
    elif simb == ')':
        parenteses.append(')')
if parenteses.count('(') != parenteses.count(')'):
    print('A expressão está incorreta!')
else:
    print('A expressão está correta!')
