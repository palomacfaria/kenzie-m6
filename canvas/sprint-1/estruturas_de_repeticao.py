# LOOPING FOR
# imprime cada elemento da lista
for elemento in [1, 2, 3]:
    print(elemento)

# imprime cada caractere da string
for caractere in "Olá, mundo!":
    print(caractere)

# imprimindo os números de 1 a 5
for i in range(1, 6):
    print(i)


# LOOPING WHILE
# imprimindo os números de 1 a 5
i = 1
while i <= 5:
    print(i)
    i += 1

# BREAK
# imprimindo os números de 1 a 5, mas interrompendo o laço quando o número é 3
for i in range(1, 6):
    if i == 3:
        break
    print(i)

# imprimindo os números de 1 a 5, pulando o número 3
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
