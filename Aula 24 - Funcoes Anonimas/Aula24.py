def funcao(arg, arg2):
    return arg * arg2

var = funcao(3,3)
print(var)

a = lambda x, y: x*y
print(a(10,10))


lista = [
    ['p4', 13],
    ['p5', 1],
    ['p3', 7],
    ['p2', 20],
    ['p1', 10],
]

lista.sort()
print(lista)

def func(item):
    return item[1]

#lista.sort(key = func)
#print(lista)

lista.sort(key = lambda item: item[1])
print(lista)

print(lista[0][0])








