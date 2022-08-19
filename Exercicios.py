i = int(input('digite um número: '))
numero = int(input('digite um número: '))
maior = numero
vezes = 0

for num in range(1, i):
    numero = int(input('digite um número: '))
    if numero > maior:
        maior = numero
        vezes = vezes + 1
print(f'O maior eh: {maior} e vezes eh {vezes}')

