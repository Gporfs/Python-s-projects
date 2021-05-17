n1=int(input('digite um número:'))
n2=int(input('digite outro numero:'))
print('Para fazer uma operação de potência usa-se ** e fica {} elevado a {} '.format(n1,n2))
p= n1**n2
print('Resultado disso é igual a {}'.format(p))
d=n1//n2
r=n1%n2 
print('Para fazer uma operação de divisão inteira usa-se // e o resto dessa divisão e para descobrir o resto da divisao usa-se o %, ficando assim {}//{} é igual(em python dois simbolos de igual um em cima do outro) a {} e o resto é igual a {} '.format(n1,n2,d,r))
print('-----ORDEM DE OPERADORES-----')
print('1-()')
print('2-**')
print('3-*,/,%,//')
print('4-+,-')
print('funções internas do python como pow entre outras não entram na ordem de precedencia.\n Para realizar raizes pode usar a potencia 1/x, sendo x a raiz que voce deseja obter.')