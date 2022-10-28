usuario = input("Digite seu usuario: ")
qtd_caracteres = len(usuario)

print(f"Usuario: {usuario}, quantidade de caracteres {qtd_caracteres}")

if(usuario.__len__() < 6):
    print("Vc precisa digitar pelo menos 6 caractetes")
else:
    print("Cadastrado com sucesso!!!")


valor = True

if valor:
    #pass => Usado para evitar erro devido ao código não implementado
    ... #Usado para evitar erro devido ao código não implementado
else:
    print("Tchau!")