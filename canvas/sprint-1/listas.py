minha_lista = [3, 'abacate', 9.7, [4, 5, 6], (1, 2, 3), None]
print(type(minha_lista))

minha_lista_2 = list('abc')
print(minha_lista_2)  # ['a', 'b', 'c']

# list não funciona para números, por isso é necessário converter para string
minha_lista_3 = list(str(123))

# range(start, stop, step)
minha_lista_4 = list(range(6))
print(minha_lista_4)

minha_lista_5 = list(range(15, 21))
print(minha_lista_5)

minha_lista_6 = list(range(15, 21, 2))
print(minha_lista_6)

# Alterando elementos de uma lista
minha_lista_7 = list(range(5))
minha_lista_7[3] = 'kenzie'
print(minha_lista_7)

# Fatiamento de listas -> nome_lista[limite_inferior, limite_superior: passo]
print(minha_lista_7[0: 3])
print(minha_lista_7[-1])
print(minha_lista_7[:4])
print(minha_lista_7[::])
print(minha_lista_7[:: 2])

# Manipulação de listas
minha_lista_8 = [1, 2, 3]
print(len(minha_lista_8))  # Retorna o tamanho da lista
print(minha_lista_8.append(4))  # Adiciona no final da lista o elemento
print(minha_lista_8.clear)  # Limpa a lista
lista_copia = minha_lista_8.copy()  # Copia a lista
print(lista_copia)

# Reordenado valores
minha_lista_9 = ['hi', 'hello', 'olá']

# sorted(key=[func], reverse=True ou False) -> Não altera os valores na lista
print(sorted(minha_lista_9))
print(minha_lista_9)

# lista.sort(key=[func], reverse=True ou False) -> Altera os valores na lista
minha_lista_9.sort()
print(minha_lista_9)

minha_lista_10 = [1, 2, 3]
print(sorted(minha_lista_10, reverse=True))  # Revertendo a ordem

minha_lista_11 = ['Melão', 'Abacaxi', 'Jabuticaba']
minha_lista_11.sort(key=len, reverse=True)
print(minha_lista_11)

# Count

minha_lista_12 = [1, 2, 3, 4, 1, 2, 1]
print(minha_lista_12.count(1))  # Conta quantas vezes aparece o elemento

minha_lista_12.extend([4, 5, 6])  # Será adicionado ao final da lista
print(minha_lista_12)

# Juntar 2 listas
juntar_listas = minha_lista_11 + minha_lista_12
print(juntar_listas)

# Buscar a primeira vez que o elemento informado aparece
print(minha_lista_12.index(2))

# POP - Remove o ultimo elemento da lista
ultimo_elemento = minha_lista_12.pop()
print(ultimo_elemento)

# POP - Remove o elemento do index informado
elemento_posicao_remove = minha_lista_12.pop(3)
print(elemento_posicao_remove)
