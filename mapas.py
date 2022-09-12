"""
Mapas -> Conhecidos em Python como dicionários

Dicionários em Python são representados por {}

# Interar sobre dicionários

for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'{chave} : {receita[chave]}')

# Acessando as chaves

print(receita.keys())
# Trás um dicionário de chaves

for chave in receita.keys():
    print(receita[chave])


# Acessando os valores

print(receita.values())
# Trás um dicionário de valores

for valor in receita.values():
    print(valor)

# Desempacotamento de dicionários

for chave,valor in receita.items():
    print(f'{chave} e valor: {valor}')


# Soma, Valor máximo, mínimo e tamanho

print(max(receita.values()))
print(sum(receita.values()))
print(min(receita.values()))
print(len(receita))
"""

receita = {'jan':100,'fev':200,'mar':230}
