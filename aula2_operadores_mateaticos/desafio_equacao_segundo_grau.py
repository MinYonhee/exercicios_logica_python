##Desafio
##Faça um programa em que você fornece os coeficientes de uma equação do segundo grau e ele retorna a raiz dessa equação (você pode considerar somente os casos em que existe a raiz real e coeficientes inteiros). y = a x^2 + b x + c; x_0 = \frac{ - b \pm \sqrt{ b^2 - 4ac } }{2a}

#Importa o módulo math para utilizar a função sqrt (raiz quadrada)
import math

#Solicita ao usuário que digite um número inteiro para o coeficiente 'a' e armazena o valor na variável 'coeficiente_a'
coeficiente_a = int(input("Por favor digite um número para o coeficiente a: "))

#Imprime uma linha em branco para separar as mensagens de solicitação para o usuário
print(" ")

#Solicita ao usuário que digite um número inteiro para o coeficiente 'b' e armazena o valor na variável 'coeficiente_b'
coeficiente_b = int(input("Por favor digite o número referente ao coeficiente b: "))

#Imprime uma linha em branco para separar as mensagens de solicitação para o usuário
print(" ")

#Solicita ao usuário que digite um número inteiro para o coeficiente 'c' e armazena o valor na variável 'coeficiente_c'
coeficiente_c = int(input("Agora insira um número para o coeficinte c: "))

#Imprime uma linha em branco para separar a mensagem de solicitação para o usuário do resultado que será exibido
print(" ")

#Calcula o delta da equação quadrática e armazena o valor na variável delta
delta = (coeficiente_b ** 2) - (4 * coeficiente_a * coeficiente_c)

#Imprime o valor de delta com uma mensagem para o usuário
print("Delta é: ", delta)

#Imprime uma linha em branco para separar as mensagens de resultado
print(" ")

#Verifica se delta é negativo ou se 'coeficiente_a' é igual a 0 (se a for igual a zero a equação se torna linear)
if delta < 0 or coeficiente_a == 0:
#Se delta for negativo ou 'coeficiente_a' for zero, imprime que a equação não possui raízes reais
  print("Sua equação não possui raízes reais")
else:
#Se delta for positivo e 'coeficiente_a' não for zero, calcula as raízes da equação quadrática
 x1 = -coeficiente_b + math.sqrt(delta) / (2 * coeficiente_a) #Calula a primeira raiz da equação aplicando a fórmula de bhaskara
 x2 = -coeficiente_b - math.sqrt(delta) / (2 * coeficiente_a) #Calcula a segunda raiz da equação aplicando a fórmula de bhaskara

#Imprime as raízes da função quadrática com uma mensagem para o usuário
 print("A raiz da sua equação é:", x1, "e", x2)
