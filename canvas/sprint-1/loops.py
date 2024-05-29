# IF
numero = 10
if numero > 0:
    print("número é positivo")

# ELIF
numero = -10
if numero > 0: 
    print("número é positivo")
elif numero < 0:
    print("numéro é negativo")

# ELSE
numero = 0
if numero > 0: 
    print("número é positivo")
elif numero < 0:
    print("numéro é negativo")
else:
    print("número é zero")

dez = 10
vinte = 20
print(dez == vinte)  # False
print(dez != vinte)  # True
print(dez > vinte)  # False
print(dez < vinte)  # True
print(dez >= vinte)  # False
print(dez <= vinte)  # True

cem = 100
duzentos = 200
trezentos = 300

print(cem < duzentos and duzentos < trezentos)  # True
print(cem < duzentos or duzentos > trezentos)  # True
print(not (cem == vinte))  # True

# FOR -> imprimindo cada elemento da lista
for numero in [1, 2, 3]:
    print(numero)

# FOR -> imprimindo cada caractere
for caractere in "Hello Kenzie!":
    print(caractere)

# FOR -> imprimindo números de 1 a 5
for i in range(1, 6):
    print(i)

# WHILE -> imprimindo números de 1 a 5
i = 1
while i <= 5:
    print(i)
    i += 1
print(i)

# BREAK -> imprimindo números de 1 a 5, porém interrompendo o laço
for i in range(1, 6):
    if i == 3:
        break
    print(i)

# CONTINUE -> imprimindo números de 1 a 5, porém interrompendo o laço
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
