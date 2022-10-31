texto = 'Texto'
lista = ['Texto', True, False, 4.5]

print(lista[0])
print(lista[3])
print(lista[2])

l1 = [1,2,3]
l2 = [4,5,6]

l1.extend((l2)) #junta as listas0
print(l1)

l1.append(10) #insere no final
print(l1)

l1.insert(0, 100) #insere de acordo com o índice
print(l1)

del(l1[0:2]) #remove do indice 0 até o 2
print(l1)

l1.pop() #remove o ultimo indice
print(l1)