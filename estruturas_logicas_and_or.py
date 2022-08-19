"""
Estruturas lógicas: AND, OR, NOT, IS(é)

Para o AND: ambos precisam ser verdadeiros
Para o OR: um ou outro precisam ser verdadeiros
Para o NOT: o valor booleano é invertido
Para o IS: o valor é comparado com o outro
"""
ativo = True
logado = False
if ativo and logado:
    print("Usuário ativo e logado no sistema")
else:
    print("Ative sua conta, acesse seu e-mail!")



ativo = False
logado = True
if ativo or logado:
    print("Está ativo ou logado!")

ativo = False
if not ativo:
    print("Por favor, ative sua conta")

ative = False
if ative is False:
    print("Ative é falso")
