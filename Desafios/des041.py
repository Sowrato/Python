from datetime import date

# Pegando o ano;
ano = date.today().year

print('\n','-'*5,'DESAFIO 041','-'*5,'\n')

ano_nasc = int(input('Me informe o ano de nascimento do atleta: '))
idade = ano - ano_nasc

if idade <= 9:
    print(f'\nO atleta tem {idade} anos e está na categoria MIRIM!')
elif idade <= 14:
    print(f'\nO atleta tem {idade} anos e está na categoria INFANTIL!')
elif idade <= 19:
    print(f'\nO atleta tem {idade} anos e está na categoria JUNIOR!')
elif idade <= 20:
    print(f'\nO atleta tem {idade} anos e está na categoria SÊNIOR!')
else:
    print(f'\nO atleta tem {idade} anos e está na categoria MASTER!')

print('\n','-'*5,'FIM DO PROGRAMA','-'*5,'\n')

# até 9 anos: Mirim
# até 14 anos: Infantil
# até 19 anos: Junior
# até 20 anos: Sênior
# acima: Master