# Programa que calcula a média entre duas notas usando condições pra decidir se o aluno passou ou não
print('\n','-'*5,'MÉDIA ENTRE DUAS NOTAS','-'*5,'\n')

# Pegando as informações do aluno
name = str(input('Qual é o seu nome? ')).title().strip()

# Pedindo as notas
nota1 = float(input(f'\n{name}, me informa a sua primeira nota: '))
nota2 = float(input('\nAgora me diga sua segunda nota: '))

# Cálculo da média
media = (nota1 + nota2) / 2

print(f'\nSua média {name}, foi de {media}')

# Mostrando se o aluno passou ou não
if media < 6.0:
    print(f'\nVocê não atingiu a nota corte, estude mais!!')
elif media >= 6.0:
    print(f'\nParabéns {name}, você atingiu a nota corte!!')

# Fim do programa
print('\n','-'*5,'FIM DO PROGRAMA','-'*5,'\n')