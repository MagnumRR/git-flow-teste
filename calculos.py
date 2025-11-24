# TESTES PARA APLICAÇÕES NO GIT

print('======= CALCULOS ========')

print('> Custos Obrigatórios Trabalhistas')

print('* FGTS (8% do salário bruto mensalmente)')
print('* INSS - 7,5 % do salário bruto')
print('* IRRF - 5% do salário bruto')
print('=========================\n')

lo = 's'
while lo == 's':
    salario = float(input('Informe o salário: R$ '))
    def calc_fgts(salario):
        return 0.08 * salario
    c_fgts = calc_fgts(salario)

    def calc_inss(salario):
        return 0.075 * salario
    c_inss = calc_inss(salario)    
    
    def calc_irrf(salario):
        return 0.05 * salario
    c_irrf = calc_irrf(salario)
    
    total = c_fgts + c_inss + c_irrf
    print('-----------------------------------------------------------')
    print(f'\t Valor do FGTS: R$ {round(c_fgts,2)}')
    print(f'\t Valor do INSS: R$ {round(c_inss,2)}')
    print(f'\t Valor do IRRF: R$ {round(c_irrf,2)}')    
    print(f'Total de impostos: R$ {round(total,2)}')    
    print('-----------------------------------------------------------\n')
    print(f'Saldo: R$ {salario - total}\n') 
    lo = input('Nova consulta s - Sim / n - Não?\n')