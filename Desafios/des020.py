from random import shuffle

print('\n','-'*5,'DESAFIO 020','-'*5,'\n')

# Pedindo os nomes
a1 = input('Primeiro aluno: ')
a2 = input('\nSegundo aluno: ')
a3 = input('\nTerceiro aluno: ')
a4 = input('\nQuarto aluno: ')

# Criando a lista
list_alunos = [a1, a2, a3, a4]

# Misturando os dados da lista usando a biblioteca RANDOM com a função SHUFFLE()
shuffle(list_alunos)

# Mostrando o resultado do sorteio da lista feito pela função SHUFFLE()
print(f'\nA sequência de apresentação dos trabalhos é: {list_alunos[0]}, {list_alunos[1]}, {list_alunos[2]} e {list_alunos[3]}')

print('\n','-'*5,'FIM DO PROGRAMA','-'*5,'\n')
