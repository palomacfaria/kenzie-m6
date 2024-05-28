numero = 10
if numero > 0:
    print("numero é positivo")
elif numero < 0:
    print("numero é negativo")
else:
    print("numero é zero")


# Operadores de igualdade
x = 10
y = 20

print(x == y)  # False
print(x != y)  # True
print(x > y)   # False
print(x < y)   # True
print(x >= y)  # False
print(x <= y)  # True

#  Operadores lógicos
a = 10
b = 20
c = 30

print(a < b and b < c)  # True
print(a < b or b > c)   # True
print(not (a == b))     # True
