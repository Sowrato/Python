print('\n','-'*5,'DESAFIO 015','-'*5,'\n')

# Pegando as informações
dias_alugados = int(input('Você alugou o carro por quantos dias? '))
distancia_km = float(input('\nQuantos quilometros você percorreu? '))

# Calculando os preços
preco_km = distancia_km * 0.15
preco_dia = dias_alugados * 60
preco_final = preco_dia + preco_km

# Imprimindos os resultados
print(f'\nVocê rodou {distancia_km} km, isso custará R${preco_km} reais.')
print(f'\nVocê alugou o carro por {dias_alugados} dias, tendo que pagar R${preco_dia} reais.')
print(f'\nSua conta é de R${preco_final} reais.')


print('\n','-'*5,'FIM DO PROGRAMA','-'*5,'\n')

# 1km = 0.15 centavos
# 5km =  x

# 1 dia = 60 reais
# 5 dia = x