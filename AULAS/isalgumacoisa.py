n=input('digite algo:')
print('Pode-se dizer que esse algo é numérico?{}'.format(n.isnumeric()))
print('Pode-se dizer que esse algo é alfabetico?{}'.format(n.isalpha()))
print('Pode-se dizer que esse algo é alfa-numérico?{}'.format(n.isalnum()))
print('Está somente em maiúsculo?{}'.format(n.isupper()))