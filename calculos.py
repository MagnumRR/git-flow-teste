# TESTES PARA APLICAÇÕES NO GIT

print('======= CALCULOS ========')

print('> Custos Obrigatórios Trabalhistas')

print('* FGTS (8% do salário bruto mensalmente)')
print('* INSS - 7,5 % do salário bruto')
print('* IRRF - 5% do salário bruto')

salario = float(input('Informe o salário: R$ '))

def calc_fgts(salario):
    return 0.08 * salario

def calc_inss(salario):
    return 0.075 * salario
    
def calc_irrf(salario):
    return 0.05 * salario

total = calc_fgts(salario) + calc_inss(salario) + calc_irrf(salario)
print('-----------------------------------------------------------')
print(f'\t Valor do FGTS: R$ {round(calc_fgts(salario),2)}')
print(f'\t Valor do INSS: R$ {round(calc_inss(salario),2)}')
print(f'\t Valor do IRRF: R$ {round(calc_irrf(salario),2)}')    

print(f'Total de impostos: R$ {round(total,2)}')    
print('-----------------------------------------------------------')
print(f'Saldo: R$ {salario - total}') 