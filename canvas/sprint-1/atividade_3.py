# Crie uma lista lista_1 dos inteiros de 6 a 20 (ambos inclusos) com range
lista_1 = list(range(6, 21))
print(lista_1)

# Imprima o último elemento da lista_1
print(lista_1[-1])

# Altere o segundo elemento de lista_1 para 'Kenzie'. Imprima lista_1
lista_1[1] = 'Kenzie'
print(lista_1)

# Utilize do fatiamento para imprimir somente os elementos de índice 2, 3 e 4
print(lista_1[2: 5])

# Adicione o seguinte valor ao final de lista_1: 'Academy'. Imprima lista_1
lista_1.append('Academy')
print(lista_1)

# Remova os items referentes aos valores 'Kenzie' e 'Academy' de lista_1
lista_1.remove("Kenzie")
lista_1.remove("Academy")
print(lista_1)

# Crie e imprima uma nova lista ordenada inversamente (lista_2)
# com base em lista_1, sem ordenar de fato a lista_1. Imprima as listas

lista_2 = sorted(lista_1, reverse=True)
print(lista_1)
print(lista_2)

# Imprima o tamanho de lista_1 e lista_2
print(len(lista_1))
print(len(lista_2))

# Retire o último item de lista_1 e lista_2. Imprima lista_1 e lista_2
lista_1.pop()
print(lista_1)
lista_2.pop()
print(lista_2)

# Retire todos os elementos tanto de lista_1 quanto de lista_2, imprima-as
lista_1.clear()
lista_2.clear()
print(lista_1, lista_2)
