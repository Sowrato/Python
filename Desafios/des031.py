print('\n','-'*5,'DESAFIO 001','-'*5,'\n')

# Pegando a distância
dis = float(input('Qual a distância em km da sua viagem? '))

# Condição de valores
if dis > 200:
    # Avisando sobre o valor a ser cobrado
    print(f'\nComo sua viagem passa de 200 km, o preço a ser cobrado será R$0,45 centavos por cada km.')
    
    # Calculando
    val_km = dis * 0.45

    # Passando preço da viagem
    print(f'\nSua viagem custará R${int(val_km)} reais.')
else:
    # Avisando sobre o valor a ser cobrado
    print(f'\nComo sua viagem não passa de 200 km, o preço a ser cobrado será R$0,50 centavos por cada km.')
    
    # Calculando
    val_km = dis * 0.50
    
    # Passando preço da viagem
    print(f'\nSua viagem custará R${int(val_km)} reais.')

print('\n','-'*5,'FIM DO PROGRAMA','-'*5,'\n')