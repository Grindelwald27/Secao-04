valor_dia = 30.00
n_dias = int(input('Quantidade de dias trabalhados: '))
valor_bruto = valor_dia * n_dias
valor_liquido = valor_bruto - (valor_bruto * 8) / 100
print(f'A quantia líquida é de R${valor_liquido}')
