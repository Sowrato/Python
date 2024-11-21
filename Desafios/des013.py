print('\n','-'*5,'DESAFIO 013','-'*5,'\n')

salario = float(input('Qual o salário do funcionário? R$'))

reaj_sal = (salario * 15) / 100

aum_sal = salario + reaj_sal

print(f'\nUm funcionário que ganhava {salario} reais, com o aumento de 15%, passa a receber R${aum_sal:.2f} reais!')

print('\n','-'*5,'FIM DO PROGRAMA','-'*5,'\n')
