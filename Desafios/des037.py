print('\n','-'*5,'DESAFIO 037','-'*5,'\n')

# Pedindo o número;
num = int(input('Digite um número: '))

base_conv = int(input(f'\nAgora eu quero que você escolha a base de conversão pra ele.\nEscolha um dos número correspondentes:\n\n[1] Binário\n[2] Octal\n[3] Hexadecimal\n\nSua escolha é: '))

if base_conv == 1:

    # Colocando o número em formato Binário;
    print(f'\nO número {num} em formato binário é {num.bit_count()}')

elif base_conv == 2:

    # Colocando em Octal;
    print(f'\nEm octal ele fica {oct(num)}')

elif base_conv == 3:

    # Colocando em formato Hexadecimal;
    print(f'\nEm formato hexadecimal fica desta forma {hex(num)}')

else:
    print('\nQue pena em, você não escolheu corretamente, fica pra próxima!')

print('\n','-'*5,'FIM DO PROGRAMA','-'*5,'\n')