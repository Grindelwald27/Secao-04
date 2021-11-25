salario_base = float(input('Informe o salário base: '))
gratificacao = (salario_base * 5) / 100
imposto = (salario_base * 7) / 100
salario = salario_base - imposto + gratificacao
print(f'O salário do funcionário é de R${salario}')
