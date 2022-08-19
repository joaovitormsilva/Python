"""
Saindo de loops com break

Mesmo funcionamento em C ou Java

"""
comparador=int(input("Digite um número: "))
for numero in range(1, 1000000):
    if numero == comparador:
        break
    else:
        print(numero)

#Exemplo 2
while True:
    comando = input("digite 'sair' para sair: ")
    if comando == 'sair':
        break
