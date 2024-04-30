##Exercício 3
##Calcule e apresente o volume de uma lata de óleo dados a altura e o diâmetro da lata. Lembre:  V=πr2A

#Importa o módulo math para utilizar a constatnte pi e outras funções matemáticas
import math

#Solicita ao usuário que digite a altura da lata e armazena o valor como um número de ponto flutuante
altura = float(input("Digite a altura da lata: "))

#Imprime uma linha em branco para separar as mensagens de solicitação para o usuário
print(" ")

#Solicita ao usuário que digite o diâmetro da lata e armazena o valor como um número de ponto flutuante
diametro = float(input("Digite o diametro da lata: "))

#Imprime uma linha em branco para separar a ultima mensagem do resultado que será apresentado a seguir
print(" ")

#Calcula o raio da lata dividindo o diametro por 2
raio = diametro / 2

#Calcula o volume da lata utilizando a fórmula matemática do volume de um cilindro
volume = math.pi * (raio ** 2) * altura

#Imprime o resultado do calculo do volume com uma mensagem para o usuário
print("O volume da sua lata é: ", volume)