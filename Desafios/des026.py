print('\n','-'*5,'DESAFIO 026','-'*5,'\n')

# Pedir uma frase para o usuário e deixando ela toda em maiúculas para trabalhar melhor;
frase = input('Digite uma frase: ').upper().strip()

# Contar quantas vezes aparece a letra A;
letra_A = frase.count('A')
first_A = frase.find('A')
last_A = frase.rfind('A') + 1

# Mostrando a quantidade de letras A, a primeira posição e a ultima posição dela;
print(f'\nSão {letra_A} letras A na frase.')
print(f'\nA primeira letra A está no indice {first_A}.')
print(f'\nA ultima letra A está no indice {last_A}.')

print('\n','-'*5,'FIM DO PROGRAMA','-'*5,'\n')
