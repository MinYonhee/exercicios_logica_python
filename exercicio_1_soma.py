##Exercício 1:
##Escreva um programa que calcula e apresenta a soma de dois números inteiros.

#Solicita ao usuário que digite um número do tipo inteiro e armazena o valor na variável 'primeiroAlgarismoSoma'
primeiroAlgarismoSoma = int(input("Por favor, digite um número: "))

#Imprime uma linha em branco para dar espaço
print(" ")

#Solicita ao usuário que digite mais um número do tipo inteiro e armazena o valor na variável segundoAlgarismoSoma
segundoAlgarismoSoma = int(input("Por favor, digite mais um número: "))

#Novamente, imprime uma linha em branco para dar espaço
print(" ")

#Calcula a soma dos dois números e imprime o resultado com uma mensagem para o usuário
print("A soma dos algarismos fornecidos é: ", primeiroAlgarismoSoma + segundoAlgarismoSoma)