print('\n','-'*5,'DESAFIO 033','-'*5,'\n')

# Informando a função do programa;
print('O seguinte programa irá pedir três números e dirá o maior e o menor.')

# Pedindo números;
n1 = float(input('\n1. Me diga o primeiro número: '))
n2 = float(input('\n2. Me diga o segundo número: '))
n3 = float(input('\n3. Me diga o tercceiro número: '))

# Condições para testar o menor;
if n1 < n2 and n1 < n3:
    print(f'\n• O número {n1} é o menor.')
elif n2 < n1 and n2 < n3:
    print(f'\n• O número {n2} é o menor.')
elif n3 < n1 and n3 < n2:
    print(f'\n• O número {n3} é o menor.')

# Colocando as condições par testar o maior;
if n1 > n2 and n1 > n3:
    print(f'\n• O número {n1} é o maior.')
elif n2 > n1 and n2 > n3:
    print(f'\n• O número {n2} é o maior.')
elif n3 > n1 and n3 > n2:
    print(f'\n• O número {n3} é o maior.')

print('\n','-'*5,'FIM DO PROGRAMA','-'*5,'\n')