from math import hypot

print('\n','-'*5,'DESAFIO 017','-'*5,'\n')

co = float(input('Me informa o comprimento do Cateto Oposto: '))
ca = float(input('\nMe informa o comprimento do Cateto Adjacente: '))

hip = hypot(co, ca)

print(f'\nO valor da Hipotenusa é {hip:.2f}.')

print('\n','-'*5,'FIM DO PROGRAMA','-'*5,'\n')
