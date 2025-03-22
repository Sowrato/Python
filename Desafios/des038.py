print('\n','-'*5,'DESAFIO 038','-'*5,'\n')

n1 = int(input('Me diga o primeiro número: '))
n2 = int(input('\nAgora o segundo número: '))

if n1 > n2:
    print(f'\nO primeiro número {n1} é maior que o segundo {n2}.')

elif n1 < n2:
    print(f'\nO segundo número {n2} é maior que o primeiro {n1}.')

elif n1 == n2:
    print(f'\nOs número são iguais.')

print('\n','-'*5,'FIM DO PROGRAMA','-'*5,'\n')