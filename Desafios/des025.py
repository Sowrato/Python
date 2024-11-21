print('\n','-'*5,'DESAFIO 025','-'*5,'\n')

# Pedir o nome;
name = input('Me diga seu nome completo: ')

# Tirar os espaços no início e no fim e, colocar em maiúculas;
name_format = name.strip().upper()

# Conferir se tem SILVA em alguma parte do nome;
validacao = 'SILVA' in name_format

# Imprimir se tem ou não, sendo TRUE se tiver e FALSE se não tiver;
print(f'\nSeu nome tem SILVA? {validacao}')

print('\n','-'*5,'FIM DO PROGRAMA','-'*5,'\n')
