print('\n','-'*5,'DESAFIO 034','-'*5,'\n')

# Explicando o programa ao usuário;
print('O programa consiste em calcular o aumento do salário de um funcionário em 10% ou 15%, dependendo das seguintes condições:\n\n• Se o salário for menor ou igual à R$1250.00,o aumento será de 15%;\n• Caso o salário seja maior que R$1250.00, o aumento será de 10%;')

# Pedindo o salário do usuário;
salario = str(input('\nInforme o seu salário e o programa irá calcular em qual dos casos você se enquaixa melhor: R$')).replace(',', '.')

# Condição de cálculo;
if float(salario) <= 1250.0:

    aum_menor = (float(salario) * 15) / 100

    print(f'\nO seu salário de R${salario} é inferio à R$1250.00, sendo assim, você terá um aumento de 15%, recebendo R${aum_menor:.1f}, ficando com R${float(salario) + aum_menor:.1f}!')

else:

    aum_maior = (float(salario) * 10) / 100

    print(f'\nO seu salario de R${salario} é superior à R$1250.00, sendo assim, você terá um aumento de 10%, recebendo R${aum_maior:.1f}, ficando com R${float(salario) + aum_maior:.1f}!')

print('\n','-'*5,'FIM DO PROGRAMA','-'*5,'\n')