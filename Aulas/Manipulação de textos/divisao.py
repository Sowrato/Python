frase = 'Curso em Vídeo Python'

# Método split() usado para separar palavras de uma cadeia de caracteres através dos espaços; 
print(f'\nO resultado é: {frase.split()}\n')

# Método join() usado para unir as palavras separadas de uma cadeia de caracteres;
print(f'\nO resultado é: {'-'.join(frase.split())}')