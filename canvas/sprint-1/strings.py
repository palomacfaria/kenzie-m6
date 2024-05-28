# Como definir strings:
minha_string = 'Hello Kenzie'
minha_string = "Hello Kenzie"
minha_string = """Hello Kenzie"""

# f'strings
f'Minha String: {minha_string}'
minha_string_formatada = f'Minha_string: {minha_string}'

# Como utilizar aspas dentro das strings sem gerar erros
minha_string = "Eu gosto de ir ao MacDonald's"
minha_string = 'Eu gosto de ir ao MacDonald\'s'

# Como contatenar strings:
string_1 = "cow"
string_2 = "boy"
string_3 = string_1 + string_2  # cowboy

# Pegar a posição da letra partindo do indice 0
string = 'Kenzie'
string[0]
string[1]

# Pegar a posição da letra partindo do indice final
string[-1]

# Pegar apenas uma parte da string definindo : start - stop - step
string = 'monty Python'
string[0:5]
string[:5]
string[6: 12]
string[0: 12: 2]
string[6:]

# Como deixar a primeira letra maiuscula
string = 'monty python'
string.capitalize()

# Contar quantas palavras ou letras possuem na variável
string.count('python')
string.count('y')

# Perguntar se a string começa com o valor informado
string.startswith('python')

# Perguntar se a string termina com o valor informado
string.endswith('python')

# Perguntar se a string só possui letras minusculas
string.islower()

# Perguntar se a string só possui letras maiúsculas
string.isupper()

# Verificar o comprimento da string
len(string)

# Deixar todos os caracters da string em caixa baixa
string.lower()

# Deixar todos os caracteres da string em caixa alta
string.upper()

# Inverter de minusculo para maiúsculo todos os valores da string
string = 'Monty Python'
string.swapcase()

# Converte o valor de toda primeira letra para maiúsculo
string = 'monty python'
string.title()

# Transformar nossa string em uma lista
string.split()
string = 'monty+python'
string.split('+')

# Substituir um trecho por outro
string = 'monty python'
string.replace('monty', 'kenzie')

# Cenntralizar a string utilizando um caractere especifico
# sintaxe -> string.center(length, caracter)
string.center(20, '*')
string.center(20, )  # Preencherá com espaços
