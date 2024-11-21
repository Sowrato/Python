print('\n','-'*5, 'DESAFIO 004', '-'*5)

msg = input('\nDigite alguma coisa: ')

print(f'O tipo primitivo é {type(msg)}')
print(f'Só tem espaços? {msg.isspace()}')
print(f'É um número? {msg.isnumeric()}')
print(f'É alfabético? {msg.isalpha()}')
print(f'É alfanumérico? {msg.isalnum()}')
print(f'Está em maiúsculas? {msg.isupper()}')
print(f'Está em minúsculas? {msg.islower()}')
print(f'Está capitalizada? {msg.capitalize()}')

print('\n','-'*5, 'FIM DO PROGRAMA', '-'*5, '\n')