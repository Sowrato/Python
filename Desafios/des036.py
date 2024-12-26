print('\n','-'*5,'DESAFIO 036','-'*5,'\n')

print('\033[1;31m', '=' * 10, ' EMPRÉSTIMO BANCÁRIO ', '=' * 10, '\033[m')

print('\n\033[1;31m•\033[m \033[36mVamos pedir algumas informações para darmos sequência no \033[1;4mEmpréstimo.\033[m')

nome = str(input('\n\033[1;31m•\033[m \033[36mComo posso te chamar? \033[1;32m'))

while nome == '':
    print('\n\033[1;7;31mNecessitamos desses dados para dar continuidade na validação do Empréstimo!\033[m')
    nome = str(input('\n\033[1;31m•\033[m \033[36mComo posso te chamar? \033[1;32m'))

idade = str(input(f'\n\033[1;31m•\033[m \033[m\033[36mPara continuarmos com a solicitação \033[1;4m{nome.capitalize()}\033[m, \033[36mpreciso saber sua idade sem falsidade: \033[1;32m'))

while idade == '':
    print('\n\033[1;7;31mNecessitamos desses dados para dar continuidade na validação do Empréstimo!\033[m')
    idade = str(input(f'\n\033[1;31m•\033[m \033[m\033[36mPara continuarmos com a solicitação \033[1;4m{nome.capitalize()}\033[m, \033[36mpreciso saber sua idade sem falsidade: \033[1;32m'))

idade = int(idade)

if idade < 18:
    print('\n\033[1;7;31mInfelizmente você é menor de idade e não pode fazer um empréstimo!\033[m')
else:
    print('\n\033[1;31m•\033[m \033[36mVamos começar!\033[m')

    salario = str(input('\n\033[1;31m•\033[m \033[1;36mInforme o seu Salário: \033[1;32mR$')).replace(',','.')

    while salario == '':
        print('\n\033[1;7;31mNecessitamos desses dados para dar continuidade na validação do Empréstimo!\033[m')
        salario = str(input('\n\033[1;31m•\033[m \033[1;36mInforme o seu Salário: \033[1;32mR$')).replace(',','.')

    salario = float(salario)

    val_casa = str(input('\n\033[1;31m•\033[m \033[36mNos diga o Valor da casa: \033[1;32mR$')).replace(',','.')

    while val_casa == '':
        print('\n\033[1;7;31mNecessitamos desses dados para dar continuidade na validação do Empréstimo!\033[m')
        val_casa = str(input('\n\033[1;31m•\033[m \033[36mNos diga o Valor da casa: \033[1;32mR$')).replace(',','.')

    val_casa = float(val_casa)

    anos = str(input('\n\033[1;31m•\033[m \033[36mEm quantos Anos pretende pagar:\033[m \033[1;32m'))

    while anos == '':
        print('\n\033[1;7;31mNecessitamos desses dados para dar continuidade na validação do Empréstimo!\033[m')
        anos = str(input('\n\033[1;31m•\033[m \033[36mEm quantos Anos pretende pagar:\033[m \033[1;32m'))
    
    anos = int(anos)

    preco_presta = val_casa / (anos * 12)

    trinta_porc = (salario * 30) / 100

    print(f'\n\033[1;31m•\033[m \033[36mO seu salário é \033[1;4m\033[1;32mR${salario:.2f} reais\033[m \033[36m e o valor da casa é \033[1;4m\033[1;32mR${val_casa:.2f} reais\033[m \033[36m, você quer pagar em \033[1;4m\033[1;32m{anos} anos\033[m \033[36m.\033[m')

    if preco_presta > trinta_porc:
        print(f'\n\033[1;31m•\033[m \033[36mO preço das suas parcelas seriam \033[1;32mR${preco_presta:.2f} reais\033[m\033[36m, sendo acima de 30% do seu salário, que corresponde à \033[1;32mR${trinta_porc:.2f} reais\033[m\033[36m.')
        print('\n\033[1;31m•\033[m \033[1;7;31mInfelizmente o empréstimo não pode ser aprovado!\033[m')
    else:
        print(f'\n\033[1;31m•\033[m \033[36mO preço das suas parcelas seriam \033[1;32mR${preco_presta:.2f} reais\033[m\033[36m, sendo acima de 30% do seu salário, que corresponde à \033[1;32mR${trinta_porc:.2f} reais\033[m\033[36m.')
        print('\n\033[1;31m•\033[m \033[1;7;32mEmpréstimo confirmado!\033[m')

print('\033[m\n','-'*5,'FIM DO PROGRAMA','-'*5,'\n')