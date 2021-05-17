# TUPLAS SÃO IMUTÁVEIS
lanche = ('Big Mac', 'Batata Frita', 'Coca Refil', 'Sundae', 'Batata Frita')

for comida in lanche:
    print(f'Comi {comida}')

for cont in range(0, len(lanche)):
    print(f'Comi {lanche[cont]}, na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Comi {comida}, na posição {pos}')

print(lanche.count('Batata Frita'))

print(lanche.index('Batata Frita'))

print(lanche.index('Batata Frita', 2))

pessoa = ('Gustavo', 17, 'M', 82.3)
print(pessoa)
del pessoa
print(pessoa)
