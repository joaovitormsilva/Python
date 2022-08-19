"""
Listas

Elas funcionam como vetores/matrizes
porém são DINÂMICOS e também podermos colocar qualquer dado.

- Dinâmico:
    - Não possui tamanho fixo, ou seja, pode-se criar a lista e ir adicionando
    elementos; (consome memória)
    - Não possuem tipo de dado fixo, pode-se colocar qualquer tipo de dado

As listas em Python são representadas por colchetes;

lista3 = list(range(13))
lista5 = list('João Vitor')

# Função que ordena a lista:
lista5.sort()
print(f'{lista5}')

# Podemos facilmente contar o número de ocorrências em uma lista
print(lista5.count('o'))

# Adionionar elementos em listas

Para adicionar elementos em listas, utilza-se a função append()

lista.append(42)
print(lista)

# OBS: Com append, nós só conseguimos adicionar 1 elemento por vez
# lista.append(12,12,31,42) # ERRO

lista.append([2, 23, 4242])  # A lista é colocada como 1 elemento
print(lista)

if [2, 23, 4242] in lista:
    print("Lista encontrada")
else:
    print("Lista não foi encontrada")

lista.extend([5161, 2312, 6156])  # coloca cada elemento separado
print(lista)

#  Podemos inserir um novo elemento indicando o indice
#  OBS: Não substitui o valor na posição, só o desloca para a proxima
lista.insert(2,'Desok')
print(lista)

lista = lista + lista2
lista.extend(lista2)
print(lista)


#  Inverter a lista com reverse e slice
lista2.reverse()
print(f'{lista2[::-1]}')

#  Copiar uma lista
lista3 = lista2.copy()
print(lista3)

#  Saber o tamanho de uma lista
print(len(lista))

# Remover o ultimo elemento de uma lista
# O POP remove o ultimo e o retorna
lista2.pop()
print(lista2)

#  Remover pelo indice
#  OBS: Se não houver elemento no indice terá um ERRO
print(lista2.pop(2))
print(lista2)

#  Remover todos os elementos de uma lista
lista2.clear()
print(lista2)

#  Repetir os elementos de uma lista

nova = [1, 2, 3]
print(nova * 3)

# converter uma string em uma lista
# OBS: Por padrão o 'split' separa os elementos pelo espaço entre elas
string = 'João vitor'
print(string.split())

string = 'João,vitor,martins,da,silva'
print(string.split(','))

#  Convertendo uma lista em uma string
lista3 = ['João', 'Vitor']
#  Abaixo estamos falando: pega a lista3 e coloca espaço entre cada elemento
curso = ' '.join(lista3)
print(curso)
# Abaixo no lugar de um espaço será um $
curso = '$'.join(lista2)
print(curso)

# iterando sobre listas

for elemento in lista2:
    print(elemento)

#  Usando while

carrinho = []
produto = ''

while produto != 'sair':
    produto = input("Adicione um produto na lista ou digite:'sair'")
    if produto != 'sair':
        carrinho.append(produto)
for elemento in carrinho:
    print(elemento)

#  Utilizando variaveis na lista

numeros = [1, 2, 3, 4, 5]
num1 = 1
num2 = 2
num3 = 3
num4 = 4
num6 = 6

numeros = [num1,num2,num3,num6]
print(numeros)

#  Fazemos acesso aos elementos através do indice
cores = ['azul', 'verde', 'amarelo', 'branco']
# Pense na lista como um circulo, onde o final da lista está ligado ao inicio
print(cores[1])  # verde
print(cores[-1])  # branco

# Gerar o indice em um for
# cores = list(enumerate(cores))
# print(cores)

for indice, cor in enumerate(cores):
    print(indice, cor)

# outros métodos úteis

#encontrar o índice de um elemento na lista
lista2 = []
for numero in range(1, 1000):
    lista2.append(numero)

# Se houver valores repetidos, ele retornará o índice do primeiro que econtrar

# Em qual índice da lista está o valor 6?
print(lista2.index(6))

# Podemos fazer busca dentro de um range, qual indice começar
print(lista2.index(6, 1))
print(lista2.index(6, 1,6))  # busca o 6 entre os indices 1 e 6

#  Revisão de slicing

# lista[inicio:fim:passo]
# range[inicio:fim:passo]

# Soma*,Valor Máximo*, Vamor Mínimo*, tamanho

# & Se os valores forem todos inteiros ou reais

lista = [1, 2, 3, 4]

print(sum(lista))  # soma
print(max(lista))   # máximo valor
print(min(lista))  # mínimo valor
print(len(lista))  # tamanho da lista

# Transformar uma lista em tupla

lista = [1, 2, 3, 4]

print(lista)
print(type(lista))
tupla = tuple(lista)
print(tupla)
print(type(tupla))

#  Desempacotamento de listas
#  OBS: Número de elementos tem que ser igual ao de variáveis
lista = [1, 2, 3]
num1, num2, num3 = lista
print(num1, num2, num3)


#  Copiando uma lista para outra (Shallow Copy e Deep Copy)

#  Forma 1 - Deep Copy

lista = [1, 2, 3, 4]
print(lista)
nova = lista.copy()
print(nova)
nova.append(5)
print(lista)
print(nova)

#  Ao utilizar o copy(), copiamos os dados da lista pra nova, e elas são independentes
#  ao mudar uma, não afeta a outra, essa forma é chamada de Deep Copy

#  Forma 2 - Shallow Copy
print('Forma 2')
lista = [1, 2, 3, 4]
print(lista)

nova = lista  # Cópia

nova.append(5)
print(lista)
print(nova)

#  A cópia via atribuição, copiamos o conteúdo de lista para nova
#  E ao modificar uma lista, ambas são modificadas, tal método é
#  chamado de Shallow Copy.
"""

lista = [0, 1, 0, 1, 2, 5, 3, 20310, 104203921]

lista.sort()
print(lista[::])
print(lista)

lista2 = ['J', 'O', 'Â', 'O', '', 'V', 'I', 'T', 'O', 'R']

cores = ['verde', 'amarelo', 'azul', 'branco']


