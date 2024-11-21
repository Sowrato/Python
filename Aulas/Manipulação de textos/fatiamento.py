frase = 'Curso em Vídeo Python'

# Serve para pegar o caracter que está no índice 9, ou qualuqer outro escolhido;
print(f'\nO resultado é: {frase[9]}\n')

# Usado para escolher um intervalo entre os índices da cadeia de caracteres;
print(f'\nO resultado é: {frase[9:13]}\n')

# Pega o índice de 9 até 21 de 2 em 2;
print(f'\nO resultado é: {frase[9:21:2]}\n')

# Quando não há nenhum número determinando o início do intervalo, ele inicia a partir do índice 0;
print(f'\nO rsulltado é: {frase[:5]}\n')

# A linha de raciocínio é o mesmo caso não tenha um número no final;
print(f'\nO resultado é: {frase[15:]}\n')

# O mesmo serve para quando for pular caracteres;
print(f'\nO resultado é: {frase[9::3]}\n') # Pulará de 3 em 3 partindo do caracter 15 até o final;
