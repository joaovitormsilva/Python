"""
Tuplas (Tuple)

Tuplas são bastante parecidas com as listas.

Existem 2 diferenças básicas:
1 - As tuplas são representadas por parênteses ()

2 - As tuplas são imutáveis: Elas não podem mudar.
todas as operações geram uma nova tupla

# CUIDADO 1: as tuplas são representadas por (), mas veja:
tupla = 1, 2, 3, 4, 5
print(type(tupla))
#  Gera uma tupla, mesmo sem ter os ()

# CUIDADO 2: Tuplas com 1 elemento
tupla2 = (3)  # Isso não é uma tupla, mas ism um inteiro
tupla2 = (3,)  # Isso sim, é uma tupla

# Conclusão: As tuplas são definidas pela vírgula , e não pelos parênteses

# Desempacotamento de uma Tupla

tupla = 'João', 'Vitor'

primeiro, segundo = tupla
print(f'{primeiro} e {segundo}')

# Métodos para adição e remoção de elementos nas tuplas, não existem
# por serem imutáveis

# Soma, Valor Máximo, Valor Mínimo e tamanho
tupla = 1, 2, 3, 3, 4, 5,

print(sum(tupla))
print(min(tupla))
print(max(tupla))
print(len(tupla))

# Concatenação de tuplas

tupla1 = 1, 2, 3, 4, 5,
tupla2 = 5, 4, 3, 2, 1,

print(tupla1 + tupla2)

# Verificar se determinado elemento está na tupla

tupla = 1, 2, 3, 4
print(3 in tupla)

# Iterando sobre uma tupla

tupla = 1, 2, 3, 4

for indice,valor in enumerate(tupla):
    print(indice, valor)

# Contando elementos na tupla

tupla = 'a', 'b', 'a', 2, 3, 2, 2

print(tupla.count(2))

nome = tuple('João Vitor')

print(nome)

# Dicas de utilização
# Deve-se usar tuplas sempre que não precisar alterar os dados
# Exemplo 1

meses = 'Janeiro','Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'julho',

# Verificamos qual indice o elemento X está na tupla

print(meses.index('Fevereiro'))

# Slicing

print(meses[::2])

# Por quê utilizar tuplas?

# Tuplas são mais rápidas do que listas.
# Tuplas deixam o código mais seguro.


tupla = 1, 2, 3,
nova = tupla # Não temos o problema de Shallow copy

outra = 4, 5, 6

print(nova)
print(tupla)
nova = nova + outra
print(nova)
print(outra)
"""

