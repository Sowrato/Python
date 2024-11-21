frase = 'Curso em Vídeo Python'

# Comando len() mostra o comprimento da cadeia de caracteres contando os espaços;
print(f'\nO resultado é: {len(frase)}\n')

# Comando frase.count('o') pede que o programa conte quantas letras 'o', minuscúlas há na frase;
print(f'\nO resultado é: {frase.count('o')}\n') # Se a letra mudar ou o seu tamanho mudar, o programa muda;

# Comando count() já com FATIAMENTO;
print(f'\nO resultado é {frase.count('o', 0, 13)}\n') # Fará com que o programa conte os caracteres no intervalo pedido, neste caso é do índice 0 até o 13;

# Comando frase.find('deo') pede que o programa procure na frase a cadeia de caracteres: 'deo', voltando o seu índice e início;
print(f'\nO resultado é: {frase.find('deo')}\n') # Se não estiver em sequência, retornará -1;

# Operador 'in' retonando TRUE ou FALSE, ou seja, verdeiro ou falso, resultado booleano;
print(f'\nO resultado é: {'Curso' in frase}\n') # Verifica se a palavra 'Curso' está na variável 'frase';

