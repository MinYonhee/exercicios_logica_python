##Exercício 2
##Escreva um programa que lê dois valores em ponto flutuante e exiba os seguintes resultados:
##Divisão do primeiro valor pelo segundo valor, sem formatação; Divisão do primeiro valor pelo segundo valor, com exatamente seis dígitos depois do ponto

#Solicita ao usuário para inserir um número e armazena na variável numero_divisao_1 como um número flutuante
numero_divisao_1 = float(input("Digite um numero: "))

#Imprime uma linha em branco para separar as mensagens de solicitação para o usuário
print(" ")

#Solicita ao usuário para inserir mais um número e armazena na variável numero_divisao_2 como um número de ponto flutuante
numero_divisao_2 = float(input("Digite mais um número: "))

#Imprime uma linha em branco para separar a solicitação do usuário da mensagem que será apresentada a seguir
print(" ")

#Calcula a divisão dos números inseridos pelo usuário e armazena na variável divisão
divisao = numero_divisao_1 / numero_divisao_2

#Imprime o resultado da divisão sem formatação dos números com uma mensagem para o usuário
print("Sua divisão exata é: ", divisao)

#Imprime uma linha em branco para separar as mensagens de resultado para o usuário
print(" ")

#Imprime o resultado da divisão dos números com apenas seis dígitos após o ponto com uma mensagem para o usuário
print("Sua divisão com apenas seis números após o ponto: {:0.6f}".format(divisao))