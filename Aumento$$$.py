print('Caso houver centavos usar PONTO e não virgula.')
s=float(input('Qual o valor do salário atual? R$'))
print('Pelo bom desempenho o salário receberá um aumento então o salário atual é: R${:.2f}'.format(s+s*15/100))