d1 = {'chave 1': 'Valor da chave 1',
      'str': 'uma string',
      2: 'chave com numero',
      'Numero': 5}

d1['Nova chave'] = 'Valor da chave'

d2 = dict(chave1 = 'Valor da chave 1')

del d1['Nova chave'] #apagando uma chave

print(d1)
print(d2)
print(5 in d1.values()) #verifica se 5 existe nos valores
print('str' in d1.keys()) #verifica se existe a chave str nas keys
print('Nova chave' in d1) #verifica se nas keys existe Nova chave
print(len(d1)) #mostra quantos pares chave valor existem

for k in d1: #acessa chaves
    print(k)

for v in d1.values(): #acessa valores
    print(v)

for v in d1.items(): #acessa chave e valor
    print(v)

for k, v in d1.items(): #acessa chave e valor
    print(k, v)

d3 = d1.copy() #cria uma copia rasa(Ainda mantem referencias do dicionario original) do dicionario na variavel

















