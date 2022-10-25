import datetime
nome = 'Natan'
idade = 32
altura = 1.74
peso = 92
anoAtual = datetime.date.today().strftime("%Y")
anoNascimento = int(anoAtual) - int(idade)
imc = float(peso) / (float(altura) ** 2)

print(f'{nome} tem {idade}, {altura} de altura e pesa {peso}')
print(f'O IMC de {nome} é {imc:.2f}')
print(f'{nome} nasceu em {anoNascimento}')

