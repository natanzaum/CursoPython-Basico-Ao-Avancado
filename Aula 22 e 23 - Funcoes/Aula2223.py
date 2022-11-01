def ola():
    print('Hello World!')

def ola2(msg = "Hello"):
    print(msg)


ola()
ola()
ola()
ola2()
ola2('AHAHAHAHA')

def testeArgs (*args, **kwargs): #kwargs = argumentos nomeados #args = argumentos no geral
    print(args)
    print("kwargs", kwargs)


testeArgs(1,2,3,4,5,6,7,8,9,10)
lista = [1,2,3,4,5]
lista2 = [6,7,8,9]

testeArgs(lista, lista2, teste = lista)

def funcao1(func2):
    print('funcao 2', func2)
    return func2

def funcao2(a1):
    print(a1)
    return a1

funcao2('aaaaaaaaa')
funcao1(funcao2)