print('\n','-'*5,'DESAFIO 012','-'*5,'\n')

val_prod = float(input('Qual o preço do produto: R$'))

desc_prod = (val_prod * 5) / 100

pre_final = val_prod - desc_prod

print(f'\nO produto que custava R${val_prod} reais, com o desconto de 5%, passa a custar R${pre_final:.2f} reais')

print('\n','-'*5,'FIM DO PROGRAMA','-'*5,'\n')