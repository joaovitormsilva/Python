"""
Loop FOR

for item in interavel:
    //execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplos de iteráveis:
String -> possibilidade de visitar cada caracter
    nome = 'João Vitor'
Lista ->
    lista = [1,2,3,4,5,6]
Range ->
    numeros = range[1,10]

nome = 'João Vitor'
lista= [1, 2, 3, 4, 5]
numeros = range(1, 10)

# Exemplo 1
for batatinha in nome:
    print(batatinha)

# Exemplo 2
for numero in lista:
    print(numero)

# Exemplo 3
for numero in range(1, 11):
    print(numero)

Enumerate:
((0,'J'),(1,'o'),(2,'ã'),(3,'o')... )

for indice, letra in enumerate(variavel):
    print(variavel[indice])
    
    
print("\n enumerate:")
for valor in enumerate(nome):
    print(valor)

qtd = int(input("Quantas vezes vai rodar? "))
for n in range(1,qtd+1):
    print(f"Imprimindo {n}")

nome = 'João Vitor'
for letra in nome:
    print(letra, end='')
"""

emoji = '\U0001F60D'

for _ in range(3):
    for num in range(1, 11):
        print(f'{emoji*num}')




