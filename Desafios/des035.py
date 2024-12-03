print('\n','-'*5,'DESAFIO 035','-'*5,'\n')

# Explicando o programa;
print('O programa irá decidir se as retas formam um triângulo.')

# Pedindo as retas;
reta1 = float(input('\n1. Informe o tamanho em metros da primeira reta: '))
reta2 = float(input('\n2. Informe o tamanho em metros da segunda reta: '))
reta3 = float(input('\n3. Informe o tamanho em metros da terceira reta: '))

# Condições
if reta1 < (reta2/2) and reta1 < (reta3/2):
    print(f'\nÉ possível fazer um triângulo.')
elif reta2 < (reta1/2) and reta2 < (reta3/2):
    print(f'\nÉ possível fazer um triângulo.')
elif reta3 < (reta1/2) and reta3 < (reta2/2):
    print(f'\nÉ possível fazer um triângulo.')
else:
    print(f'\nNão é possível fazer um triângulo.')

print('\n','-'*5,'FIM DO PROGRAMA','-'*5,'\n')