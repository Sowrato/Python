print('\n','-'*5,'DESAFIO 022','-'*5,'\n')

# Pedindo o nome;
nome = input('Me diga seu nome: ')

# Cortando os espaços que estivere no começo e no fim; deixando as inicias de cada nome maiúculas;
nome_format = nome.strip().title()

print(f'\nSeu nome é: {nome_format}')
print(f'\nTodas as letras maiúsculas: {nome_format.upper()}') # Nome em maiúculas;
print(f'\nTodas as letras minúsculas: {nome_format.lower()}') # Nome em minúculas;

# Separando nome e sobrenomes e, colocando-os em uma lista;
nome__list = nome_format.split()

# Juntando todos os nomes das listas sem colocar nenhum espaço entre eles;
nome = ''.join(nome__list)

# Contando a quantidade de caracteres presentes em todo o nome sem contar os espaços;
print(f'\nSeu nome inteiro tem {len(nome)} letras.')

# Mostrando a quantidade de caracteres que há apenas no primeiro nome;
print(f'\nSeu primeiro nome({nome__list[0]}) tem {len(nome__list[0])}')

print('\n','-'*5,'FIM DO PROGRAMA','-'*5,'\n')