print('\n','-'*5,'DESAFIO 040','-'*5,'\n')

# Pedindo as notas;
nota1 = float(input('Me informe sua primeira nota: '))
nota2 = float(input('\nMe informe sua segunda nota: '))

# Calculando a média;
media = (nota1 + nota2) / 2

# Condições;
if media < 5.0:
    print(f'\nInfelizmente você ficou abaixo da média com {media}, então está REPROVADO!')
elif media < 7.0:
    print(f'\nCom a sua média de {media}, você está de RECUPERAÇÃO!')
elif media >= 7.0:
    print(f'\nParabéns, você atingiu a média com {media} e está APROVADO!')

# abaixo 5.0
# entre 5.0 e 6.9
# igual ou acima 7.0

print('\n','-'*5,'FIM DO PROGRAMA','-'*5,'\n')