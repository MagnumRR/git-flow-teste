# TESTES PARA APLICAÇÕES NO GIT

print('-------- CALCULOS --------')

print('Custos Obrigatórios Trabalhistas')

print('FGTS (8% do salário bruto mensalmente)')
print('INSS - 7,5 % do salário bruto')
print('IRRF - 5% do salário bruto')

salario = float(input('Informe o salário: '))

def calc_fgts(salario):
    return 0.08 * salario

def calc_inss(salario):
    return 0.075 * salario
    
def calc_IRRF(salario):
    return 0.05 * salario

    