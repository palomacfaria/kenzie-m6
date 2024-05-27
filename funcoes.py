# *Criando funções com parâmetros

def soma(parametro1, parametro2):
    return parametro1 + parametro2


resultado = soma(4, 5)  # parametro1 -> 4 | parametro2 -> 5
print(resultado)
# 9

# *Não definindo os valores por parâmetro


def soma2(parametro1, parametro2=0):
    return parametro1 + parametro2


resultado = soma2(100)  # Usa o valor padrão de parametro2 (0)
print(resultado)
# 100


# *Argumentos Nomeados
def calcular_preco(preco, desconto):
    return preco * (1 - desconto)


preco_final = calcular_preco(preco=100, desconto=0.1)

preco_final = calcular_preco(100, desconto=0.1)


# *Auxiliar pass
# cria uma função vazia
def minha_funcao():
    pass


# cria uma função vazia da mesma forma
def minha_funcao2():
    ...


# cria um loop vazio
for x in range(10):
    pass


# cria uma classe vazia
class MinhaClasse:
    pass

# *Funções builtins
# conversão de inteiro para booleano


my_bool = bool(0)
print(my_bool)
# False

# conversão de inteiro para string
my_str = str(400)
print(my_str)
# '400'

# conversão de inteiro para decimal
my_float = float(7)
print(my_float)
# 7.0

# conversão de string para inteiro
my_int = int("14")
print(my_int)
# 14

# verificar tamanho de uma estrutura sequencial
my_str = 'Kenzie Academy Brasil'
len(my_str)
# 21
