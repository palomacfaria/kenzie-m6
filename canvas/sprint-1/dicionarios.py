meu_dicionario = {}
print(type(meu_dicionario))

# *Acessar o valor pela chave
meu_dicionario = {'chave': 'valor'}
print(meu_dicionario['chave'])

# *Criando dicionário com a função dict
meu_dicionario = dict(chave="valor")
print(meu_dicionario)  # Resposta: {'chave': 'valor'}

meu_dicionario = dict([('primeiro', 1), ('segundo', 2), ('terceiro', 3)])
print(meu_dicionario)  # Resposta: {'primeiro': 1, 'segundo': 2, 'terceiro': 3}

# *Função ZIP - Junta os elementos como chave e valor
lista = ['primeiro', 'segundo', 'terceiro']
lista_2 = [1, 2, 3]
meu_dicionario = dict(zip(lista, lista_2))
print(meu_dicionario)  # Resposta: {'primeiro': 1, 'segundo': 2, 'terceiro': 3}

# *Criando dicionário com um único valor
chaves = ['primeiro', 'segundo', 'terceiro']
valor = 0
meu_dicionario = dict.fromkeys(chaves, valor)
print(meu_dicionario)  # Resposta: {'primeiro': 0, 'segundo': 0, 'terceiro': 0}

# *Acessando elemento pela posição da chave
meu_dicionario = dict(primeiro=1, segundo=2, terceiro='terceiro')
print(meu_dicionario['segundo'])  # Resposta: 2

# *Acessando valores com o método get
print(meu_dicionario.get('segundo'))  # Resposta: 2

# *Acessando um valor que não existe com o método get
print(meu_dicionario.get('quarto'))  # Resposta: None

# Colocando um valor default quando o elemento não existe
print(meu_dicionario.get('quarto', 'chave não encontrada'))

# *Acessar todas as chaves que o dicionário tem
print(meu_dicionario.keys())

# *Acessar todos os valores que o dicionário tem
print(meu_dicionario.values())

# *Acessar tosos os elementos (chave e valor)
print(meu_dicionario.items())

# *Adicionar elementos
meu_dicionario['quarto'] = 4
print(meu_dicionario)

# *Atualizar elementos
meu_dicionario['quarto'] = 5
print(meu_dicionario)

# *Adicionar elementos com o método UPDATE
meu_dicionario.update({'quinto': 5})
print(meu_dicionario)

# *Atualizando elementos com o método UPDATE
meu_dicionario.update({'quinto': 6})
print(meu_dicionario)

# *Excluir elementos com del
del meu_dicionario['primeiro']
print(meu_dicionario)

# *Excluir elementos com POP
meu_dicionario.pop('quarto')
print(meu_dicionario)

# *Excluir ultimo elemento
meu_dicionario.popitem()
print(meu_dicionario)

# *Excluir todos os elementos do dicionário
meu_dicionario.clear()
print(meu_dicionario)