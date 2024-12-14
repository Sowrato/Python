formatacao = {'negrito': '\033[1m',
              'negativo': '\033[7m'}

cores = {'limpa': '\033[m',
        'vermelho': '\033[31m',
        'amarelo': '\033[33m'}

print('\n\033[1;7;31m ATENÇÃO \033[m\n')

print(f'O {formatacao["negrito"]}{formatacao["negativo"]}Aviso{cores["limpa"]} a seguir irá apenas mostrar a formatação {cores["amarelo"]}kkkkkkkk{cores["limpa"]}\n')