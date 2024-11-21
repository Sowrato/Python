frase = 'Curso em Vídeo Python'

# Comando replace() busca a palavra pedida e substitui por outra pedida;
print(f'\nO resultado é: {frase.replace('Python', 'Android')}\n') # Neste caso, a palavra 'PYTHON' foi substituída por 'ANDROID';

# Método upper() faz com que as letras minúsculas fiquem maiúsculas, as que já são, permanecem;
print(f'\nO resultado é: {frase.upper()}\n')

# Método lower() faz com que as letras maiúsculas fiquem minúsculas, as que já são, permanecem;
print(f'\nO resultado é: {frase.lower()}\n')

# Método capitalize() faz com que apenas a primeira letra fique maiúscula;
print(f'\nO resultado é: {frase.capitalize()}\n')

# Método title() faz cada letra inicial ficar maiúculas;
print(f'\nO resultado é: {frase.title()}\n')

frase = '   Aprenda Python  '

# Método strip() apaga os espaços que estiverem no início e no final da String;
print(f'\nO resultado é: {frase.strip()}\n')

# Método rstrip() apaga apenas os espaços que estiverem apenas no final da String;
print(f'\nO resultado é: {frase.rstrip()}\n')

# Método lstrip() apaga apenas os espaços que estiverem apenas no início da String;
print(f'\nO resultado é: {frase.lstrip()}\n')
