print("Digite seu nome")
nome = input()

print("Digite sua altura")
altura = float(input())

print("Digite seu peso")
peso = float(input())

print(nome, "seu imc é: ", peso / (altura ** 2))
