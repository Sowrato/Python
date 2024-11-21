print('\n','-'*5,'DESAFIO 024','-'*5,'\n')

# Pedindo o nome da cidade do usuário;
cidade = input('Me diga o nome da sua cidade: ')

# Separand em uma lista;
cidade_list = cidade.split()

# Conferindo se começa com SANTO no nome;
validacao = 'SANTO' in cidade_list[0].upper()

# Imprimindo a confirmação;
print(f'\nSua cidade começa com SANTO? {validacao}')

print('\n','-'*5,'FIM DO PROGRAMA','-'*5,'\n')
