# Usando a biblioteca RANDOM e importando o comando RANDINT para pegar um número INTEIRO;
from random import randint

print('\n','-'*5,'DESAFIO 028','-'*5,'\n')

# Pedir valor entre 0 e 5 ao computador;
num_comp = randint(0, 5)

# Propondo desafio;
print('Um desafio te aguarda Jogador!\nO Computador está querendo testar a sua sorte, ele escolheu um valor que está entre 0 e 5, incluindo o 0 e 5 também!\nE está desafiando você a descobrir o número que ele escolheu, todos os outro jogadores foram humilhados.\nBoa sorte!\n')

# Pedindo nome do usuário;
jogador = str(input('Mas antes de testar a sua sorte, me diga seu nome Jogador: ')).title().strip()

# Saudando o jogador;
resp = str(input(f'\nSe prepare para o desafio {jogador}, podemos começar? '))

# Formatando a resposta;
resp = resp.title().strip()

# Condição validando a resposta do jogador;
if resp != 'Sim':
    print(f'\nQue pena, não era isso que eu estava esperando ouvir! Volte depois então {jogador}!')
else:

    print('\nEntão vamos começar!\n')

    # Colocando o COMPUTADOR como um vilão, pra dar uma diversão pro usuário kkkkkkkkk;
    print(f'COMPUTADOR:\n\n"Mais um querendo me vencer, vai virar mais um humilhado!!\nVamos ver se você está pronto pra me vencer {jogador}!\nMeu número eu já escolhi, agora tente acertar! Hahahaha"')

    # Pegando o número do usuário;
    num_jog = int(input(f'\nAudacioso esse Computador né {jogador}, agora é com você Jogador, que número ele escolheu?\nEle escolheu o '))

    # Verificando o número e se é igual ao escolhido;
    if num_jog < 0 or num_jog > 5: 

        # Mensagem se o jogador não escolher um número entre 0 e 5;
        print(f'\nNãããããoooo {jogador}!\nEscolha um número entre 0 e 5, podendo ser o 0 ou o 5.\nDevido o seu erro, os Jogadores perderam e o Computador continua os humilhando!')
        print(f'\nCOMPUTADOR:\n\n"Não fique triste Jogador, você foi apenas mais um humilhado para a minha coleção! Hahahaha\nBoa sorte na próxima {jogador}!"')
    
    elif num_jog != num_comp:

        # Mensagem se o jogador errar o número do computador;
        print(f'\nInfelizmente você errou {jogador}, o Computador continuará humilhando todos os Jogadores!\nVá e se fortaleça, volte mais forte para derrotá-lo na próxima!')
        print(f'\nCOMPUTADOR:\n\n"Ai, ai, ai! Mais um fracote tentando a sorte, meu número era {num_comp}!\nÉ {jogador}, você até tentou, mas não adianta tentar e falhar, some daqui fracote! Hahahaha\nSó uma coisinha, boa sorte na próxima, Jogador!"')
        
    else:

        # Mensagem quando o jogador acertar
        print(f'\nParabéns {jogador}, a única pessoa que enfrentou esse Computador e conseguiu sair com a Vitória!\nO Computador não atormentará mais os Jogadores graças a você!')
        print(f'\nCOMPUTADOR:\n\n"Parabéns {jogador}, você até que mandou bem, não vou mais atormentar seus companheiros!\nMas saiba de uma coisa, esse não é o fim, vocês podem ter ganhado a luta, mas a glória de ganhar a guerra será minha!\nMe aguarde, eu voltareeeiiii!!"')

print('\n','-'*5,'FIM DO PROGRAMA','-'*5,'\n')
