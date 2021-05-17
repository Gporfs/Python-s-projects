times = ('Internacional', 'Flamengo', 'Atlético-MG', 'São Paulo',
         'Fluminense', 'Palmeiras', 'Grêmio', 'Santos', 'Athlético-PR',
         'Corinthians', 'Bragantino', 'Ceará-SC', 'Atlético-GO', 'Sport Recife',
         'Fortaleza', 'Bahia', 'Vasco', 'Goiás', 'Coritiba', 'Botafogo')
titulo = 'BRASILEIRÃO 2021'
print('='*30)
print(f'{titulo:^30}')
print('='*30)
print('OS PRIMEIROS COLOCADOS DO BRASILEIRÃO SÃO:')
cont = 0
tops = 0
while not tops == 5:
    print(times[tops])
    tops += 1
print('OS ULTIMOS COLOCADOS SÃO:')
loosers = -1
while not loosers == -5:
    print(times[loosers])
    loosers -= 1
print('INTEGRANTES DESSE BRASILEIRAO:')
for t in sorted(times):
    print(f'{t}')
time = str(input('Qual time você quer saber a posição? ')).title()
while time not in times:
    time = str(input('Tente de novo. Qual time você quer saber a posição? '))
chapeco = times.index(time) + 1
print(f'{time} se encontra na posição {chapeco}ª posição do Brasileirão!')
