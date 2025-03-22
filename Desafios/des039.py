from datetime import date

# Configurando a data;
ano = date.today().year

print('\n','-'*5,'DESAFIO 039','-'*5,'\n')

# Pegando o ano de nascimento;
ano_nasc = int(input('Me informe o seu ano de nascimento: '))

# Calculando a idade;
idade = ano - ano_nasc
falta_anos = 18 - idade

if idade < 18:

    print(f'\nVocê tem ou vai fazer {idade}, ainda não pode se Alistar!\nPrecisa esperar {falta_anos} anos para se Alistar!')

elif idade == 18:

    print(f'\nVocê já possui 18 anos, já pode se Alistar!')

elif idade > 18:

    print(f'\nVocê já passou da idade de se Alistar, precisa comparecer a uma junta militar resolver a sua situação!')

print('\n','-'*5,'FIM DO PROGRAMA','-'*5,'\n')