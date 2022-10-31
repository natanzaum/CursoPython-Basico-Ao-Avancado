print('Tabuada')
x = 1
y = 1

while x <= 10:
    while y <= 10:
        print(f'{x} X {y} = {x * y}')
        y = y + 1
    x = x + 1
    y = 0


a = 1
while a <= 1000:
    print(a)
    a +=1
else: #entra no else depois q a condição do çao fica falsa. Se usar o brak ele pula o else tb!
    print("Terminei!!!!")

frase = 'O rato roeu a roupa do rei de Roma'
contador = 0

while contador < len(frase):
    print(frase[contador], contador)
    contador += 1