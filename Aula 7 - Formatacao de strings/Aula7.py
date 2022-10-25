#f strings
nome = "Natan" #tipagem dinamica, define em tempo de compilação.
print(nome)
idade = 32
altura = 1.74
print("Idade:", idade, "Altura:", altura)
maiorque18 = idade > 18
print("É maior de idade:", maiorque18)
imc = 24.58786521445566

print(f'{idade} - {nome} - idade e nome do cidadão! IMC => {imc:.2f}')
print('{0} - {1} - idade e nome do cidadão! IMC => {2}'.format(idade, nome, imc))
print('{} - {} - idade e nome do cidadão! IMC => {:.2f}'.format(idade, nome, imc))