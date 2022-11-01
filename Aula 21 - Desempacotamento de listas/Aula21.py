lista = ['Luiz', 'jose', 'Pedro']
n1, n2, n3 = lista
print(n1, n2, n3)

lista = ['Luiz', 'jose', 'Pedro', 1,2 ,3 ,4 ,5 , 6, 7 ,8 ,9, 100]

n1, n2, n3, *outra_lista, ultimo_da_lista = lista
print(n1, n2, n3,  ultimo_da_lista)
print(outra_lista)

#Invertendo o valor de variaveis
x = 10
y = 'Natan'

x , y = y, x
print(f'X = {x} e Y = {y}')

#operador ternário em python

logged_user = False

if logged_user:
    print("Ta logado hehe")
else:
    print("precisa logar mano!")

msg = 'Usuario logado' if logged_user else 'Precisa logar!'
print (msg)

