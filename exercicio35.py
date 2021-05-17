sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()
while sexo not in 'MmFf':
    sexo = str(input('\033[31mOpção inválida.\033[m Informe seu sexo [M/F]: ')).upper().strip()
