valor = float(input('Digite o valor a ser sacado: R$'))
total = valor
totced = 0
cedula = 50
while True:
    if total >= cedula:
        total -= cedula
        totced += 1
    else:
        if totced >= 1:
            print(f'Você receberá {totced} cédulas de {cedula}!')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totced = 0
        if total == 0:
            break
