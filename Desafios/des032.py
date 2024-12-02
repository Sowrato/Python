from datetime import date

print('\n','-'*5,'DESAFIO 032','-'*5,'\n')

ano = int(input('Me diga um ano ou digite 0: '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'\nO ano {ano} é BISSEXTO')
else:
    print(f'\nO ano {ano} NÃO é BISSEXTO')

print('\n','-'*5,'FIM DO PROGRAMA','-'*5,'\n')