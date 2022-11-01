cpf = input('Digite o CPF: ')

while cpf.__len__() > 14 or cpf.__len__() <= 0:
    print('CPF Inválido!!!')
    cpf = input('Digite o CPF: ')

cpf_formatado = ''

if cpf.__len__() > 11:
    for n, caractere in enumerate(cpf):
        if caractere == '.' or caractere =='-':
            continue;
        cpf_formatado += caractere
    cpf = cpf_formatado

digito_1 = 0
contador = 10
somatorio = 0

for numero in cpf:
    somatorio += int(numero) * contador
    contador -= 1
    if contador < 2:
        break

digito_1 = 11 - (somatorio % 11)
if digito_1 > 9:
    digito_1 = 0

contador = 11
somatorio = 0

for numero in cpf:
    somatorio += int(numero) * contador
    contador -= 1
    if contador < 2:
        break

digito_2 = 11 - (somatorio % 11)
if digito_2 > 9:
    digito_2 = 0

novo_cpf = cpf[0:9] + str(digito_1) + str(digito_2)

if cpf == novo_cpf:
    print('CPF válido')
else:
    print('CPF invalido')




