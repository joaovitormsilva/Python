"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionários Python
são conhecidos por mapas.

Eles são coleções do tipo chave/valor.

Dicionários são representados por chaves {}

OBS: - Chave e valor são separados por dois pontos 'chave:valor'
    - Ambo podem ser de qualquer tipo de dado
    - Pode misturar tipos de dados

# Criação de dicionários

# Forma 1

paises = { 'br': 'brasil', 'eua': 'Estados Unidos', 'pt': 'Portugal'}

print(paises)
print(type(paises))

# Forma 2

paises = dict(br='Brasil', eua='Estados Unidos', pt = 'Portugal')

print(paises)


paises = { 'br': 'brasil', 'eua': 'Estados Unidos', 'pt': 'Portugal'}

# Acessando elementos

# Forma 1: Acessando via chave

print(paises['br'])

# Forma 2: Acessando via get (Recomendado)

print(paises.get('ru'))

russia = paises.get('ru')

if russia:
    print(('tem russia'))
else:
    print('Não tem russia')

# Podemos definir um valor padrão para caso não encontremos o
# objeto com a chave informada

russia = paises.get('ru', 'Não encontrado') # pega o país da chave
# 'ru', caso não encontre retorne 'Não encontrado'

"""

paises = {'br': 'brasil', 'eua': 'Estados Unidos', 'pt': 'Portugal'}
