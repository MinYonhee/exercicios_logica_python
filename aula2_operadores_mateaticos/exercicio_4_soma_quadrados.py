##Exercício 4
##Escreva um programa que receba três números inteiros quaisquer e apresente:
###A soma dos quadrados dos três números; O quadrado da soma dos três números.

#Solicita ao usuário que digite um número inteiro e armazena o valor na variável numero_soma_1
numero_soma_1 = int(input("Digite um número: "))

#Imprime uma linha em branco para separar as mensagens para o usuário
print(" ")

#Solicita ao usuário que digite mais um número inteiro e armazena o valor na variável numero_soma_2
numero_soma_2 = int(input("Digite mais um número: "))

#Imprime uma linha em branco para separar as mensagens para o usuário
print(" ")

#Solicita ao usuário que digite mais um número inteiro para finalizar e armazena o valor na variável numero_soma_3
numero_soma_3 = int(input("Digite o número final: "))

#Imprime uma linha em branco para separar as mensagens para o usuário
print(" ")

#Calcula a soma dos quadrados dos 3 números digitados pelo usuário e armazena o resultado na variável soma
soma_quadrados = (numero_soma_1 ** 2) + (numero_soma_2 ** 2) + (numero_soma_3 ** 2)

#Imprime a soma dos quadrados dos 3 números digitados pelo usuário com uma mensagem na tela
print("A soma dos quadrados dos três números é: ", soma_quadrados)

#Imprime uma linha para separar as mensagens de retorno para o usuário
print(" ")

#Calcula o quadrado da soma dos 3 números apresentados pelo usuário e armazena o resultado na variável quadrado
quadrado_soma = soma_quadrados ** 2

#Imprime o quadrado da soma dos 3 números escolhidos pelo usuário com uma mensagem na tela
print("O quadrado da soma dos três números é: ", quadrado_soma)