print('\n','-'*5,'DESAFIO 030','-'*5,'\n')

# Pedindo valor;
num = float(input('Diga um valor: '))

# Definindo o resultado
res = num % 2

# Condição de PAR e ÍMPAR;
if res == 0:
    # Definindo como par;
    print(f'\nO número {num} é PAR!')

else:
    # Definindo como ímpar;
    print(f'\nO número {num} é ÍMPAR!')

print('\n','-'*5,'FIM DO PROGRAMA','-'*5,'\n')
