def corresponding_parenthesis(parenthesis):
    count = 0
    length = len(parenthesis)

    for position in range(length - 1):
        if parenthesis[position] == "(" and parenthesis[position + 1] == ")":
            count += 1
    return count


# Exemplo 1
result = corresponding_parenthesis("()()")
print(result)

# Exemplo 2
result = corresponding_parenthesis("()))")
print(result)

# Exemplo 3
result = corresponding_parenthesis(")))(((((")
print(result)


def remove_more_than_two_repetitions(text):
    result = []
    count = 1

    # Adicionar o primeiro caractere à result
    result.append(text[0])

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
            if count <= 2:
                result.append(text[i])
        else:
            count = 1
            result.append(text[i])

    return ''.join(result)


# Exemplo
text = "Ollloco meuuuu, taaa peegaando fogoo biiiiichooo"
text = remove_more_than_two_repetitions(text)
print(text)
