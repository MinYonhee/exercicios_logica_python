##Exercício 1
##Escreva um programa que lê dois valores inteiros e exibe os seguintes resultados: 
###O resultado do primeiro número dividido pelo segundo número; O resultado da divisão truncada do primeiro número pelo segundo número

#Solicita ao usuário para inserir um número inteiro e armazena na variável numero_divisao_1
numero_divisao_1 = int(input("Digite um número inteiro: "))

#Imprime um espaço vazio para separar o primeiro comando do segundo comando
print(" ")

#Solicita ao usuário para digitar mais um número inteiro e armazena na variável numero_divisao_2
numero_divisao_2 = int(input("Digite outro número inteiro: "))

#Imprime um espaço vazio para separar a última mensagem exibida da próxima que será aparesentada para o usuário
print(" ")

#Calcula a divisão dos números digitados pelo usuário e armazena na variável divisao
divisao = numero_divisao_1 / numero_divisao_2

#Imprime o resultado da divisão dos números com uma mensagem para o usuário
print("A divisão dos números é: ", divisao)

#Imprime um espaço em branco para separar o resultado acima do que ainda será apresentado para o usuário
print(" ")

#Calcula a divisão truncada dos números digitados pelo usuário e armazena o resultado na variável truncado
truncado = numero_divisao_1 // numero_divisao_2

#Imprime o resultado da divisão truncada dos números com uma mensagem para o usuário
print("Sua divsão truncada é: ", truncado)
