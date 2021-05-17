while True:
    n = int(input('Insira o número da tabuada que você deseja: '))
    if n < 0:
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
