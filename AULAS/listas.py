lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
print(f'A lista:{lanche}')
lanche[3] = 'picolé'
print(f'Substituindo um elemento: {lanche}')
lanche.append('cookie')
print(f'Adicionando um elemento: {lanche}')
lanche.insert(0, 'pizza')
print(f'Inserindo um novo elemento: {lanche}')
if 'pizza' in lanche:
    lanche.remove('pizza')
print(f'A lista com a remoção especifica do elemento "pizza": {lanche}')
del lanche[3]  # ou lanche.pop[3] ou lanche.remove('pizza')
print(f'Deletando o elemento na posição[3]: {lanche}')
lanche.pop()
print(f'Deletando o ultimo elemento: {lanche}')
valores = list(range(4, 11))
print(valores)
valores = [8, 2, 5, 4, 9, 3, 0]
print(valores)
valores.sort()
print(valores)
valores.sort(reverse=True)
print(valores)
for v in valores:
    print(f'{v}', end=' ')
print(f'\n{len(valores)}')
for pos, v in enumerate(valores):
    print(f'Encontrei o valor {v} na posição {pos}')
valores = []
for c in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print(valores)
valores1 = valores
print(f'valores1 recebeu uma ligação com valores: {valores1}')
valores1[0] = 0
print('Valores1[0] = 0')
print(f'valores: {valores}')
print(f'valores1: {valores1}')
