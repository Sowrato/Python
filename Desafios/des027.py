print('\n','-'*5,'DESAFIO 027','-'*5,'\n')

# Pedir o nome completo da pessoa e colocando em uma lista;
name = input('Me diga seu nome completo: ').title().split()

# Imprimir o primeiro e o ultimo nome;
print(f'\nSeu primeiro nome é {name[0]}')
print(f'\nSeu ultimo nome é {name[len(name) - 1]}')

print('\n','-'*5,'FIM DO PROGRAMA','-'*5,'\n')
