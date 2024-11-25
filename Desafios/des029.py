print('\n','-'*5,'DESAFIO 029','-'*5,'\n')

# Pedindo a velocidade de um carro;
vel = int(input(f'Qual a velocidade do carro? '))

# Condição de MULTA;
if vel > 80:

    cal_mul = (7 * (vel - 80)) / 1

    print(f'\nSe o seu carro está a uma velocidade de {vel}km/h.\nVocê está Multado e pagará R${int(cal_mul)},00 reais!')
else:
    print(f'\nO seu carro está dentro do limite de velocidade!')

print('\n','-'*5,'FIM DO PROGRAMA','-'*5,'\n')