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

print('br' in paises)# true
print('Estados Unidos' in paises)# false

if 'br' in paises:
    brasil = paises['br']

print(brasil)


localidades = {
    (23.4232323, 230123.231): 'Escritório em Tókio',
    (12.12312, 123.123): 'Escritório em NY',
    (32.412321,233.121): 'Escritório em São Paulo',
}
print(localidades)

# Adicionar elementos em um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)

# Forma 1 - Mais comum

receita ['abril'] = 350
print(receita)

# Forma 2

novo_dado = {'mai': 500}
receita.update(novo_dado)
print(receita)

# Atualizando dados em um dicionário

receita['mai'] = 550
print(receita)

# Conclusão: A forma de adicionar elemento e atualizar um, é a mesma
# Em dicionários, não pode haver chaves repetidas

# Removendo dados de um dicionário
receita = {'jan': 100, 'fev': 120, 'mar': 300}

# Forma 1
ret = receita.pop('mar')
print(ret)
print(receita)

# OBS: Informamos a chave, e terá ERRO se não achar o elemento
# Ao removermos um objeto, o valor deste objeto é sempre retornado

# Forma 2

del receita['fev']
print(receita)



# Imagine que você tem um comércio eletrônico

Carrinho de Compras:
    Produto 1:
        - nome;
        - quantidade;
        - preço;
    Produto 2:
        - nome;
        - quantidade;
        - preço;

# 1 - Utilizando uma lista para isso

carrinho = []

produto1 = ['Playstation', 1, 2300.00]
produto2 = ['Jogo', 1, 140.00]

carrinho.append(produto1)
carrinho.append((produto2))

print(carrinho)

# Teríamos que saber qual é o índice de cada informação do produto

# 2 - Poderíamos uma Tupla

produto1 = 'Playstation', 1, 2300.0
produto2 = 'Jogo', 1, 140.00

carrinho = (produto1,produto2)
print(carrinho)
# Teríamos que saber qual é o índice de cada informação do produto

# 3 - Utilizando um dicionário

carrinho = []

produto1 = {'nome': 'Playstation 4', 'quantidade':'1','preço': 2300.00}
carrinho.append(produto1)
print(carrinho)

# Desta forma, facilmente adicionamos ou removemos produtos
# do carrinho e em cada um tem-se a certeza da informação

# Métodos de dicionários

d = dict(a=2, b=3, c=4)
print(d)

#Limpar o dicionário

d.clear()
print(d)

# Copiando um dicionario para outro

# Forma 1 - Deep Copy
novo = d.copy()
novo['d'] = 4
print(novo)

# Forma 2 - Shallow Copy

novo = d
novo['d'] = 4
print(d)
print(novo)
"""

# Métodos de dicionários

d = dict(a=2, b=3, c=4)
print(d)

# Forma não usual de criação de dicionários

outro = {}.fromkeys(['aawdad','sdwaeaes','c'], 'desconhecido')
print(outro)

# O método fromkeys recebe dois parâmetro: um interável e um valor
# ele gera para cada valor, uma chave q irá atribuir a chave

veja = {}.fromkeys('teste','valor')
print(veja)

desconhecido = {}.fromkeys(['vitima1','vitima2','vitima3'],'desconhecido')

print(desconhecido)

veja = {}.fromkeys(range(1,11),'novo')

print(veja)