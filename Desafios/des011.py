print('\n','-'*5,'DESAFIO 011','-'*5,'\n')

# Pegando os valores da parede
alt_par = float(input('Me informa a altura da sua parede em metros: '))
larg_par = float(input('Me informa a largura da sua parede em metros: '))

# Definindo a Área da parede
area_par = alt_par * larg_par

# 1L pinta 2m²
ltr_tin = area_par / 2

print(f'\nVocê tem uma parede de {area_par:.2f} metros quadrados!')
print(f'\nSe 1 Litro de tinta pinta 2 metros quadrados:')
print(f'\nEntão vai ser preciso {ltr_tin:.2f} Litros de tinta pra pintar toda a sua parede!\n')

print('\n','-'*5,'FIM DO PROGRAMA','-'*5,'\n')