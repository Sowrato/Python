from random import randint

print('\n','-'*5,'DESAFIO 023','-'*5,'\n')

# Pedir o número
num = randint(0, 1001)

# Mostrando o número fornecido
print(f'O número sorteado foi: {num}')

# Pegando unidade, dezena, centena e milhar
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'\nEste número tem {u} unidades.')
print(f'\nEste número tem {d} dezenas.')
print(f'\nEste número tem {c} centenas.')
print(f'\nEste número tem {m} milhares.')

print('\n','-'*5,'FIM DO PROGRAMA','-'*5,'\n')
