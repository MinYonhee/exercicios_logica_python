##Exercício 2:
##Faça um programa que, informado o tamanho do lado de um quadrado, informa a sua área e o seu perímetro.

#Solicita ao usuário que digite o valor do lado do quadrado e armazena o valor em uma variável do tipo ponto flutuante (float)
ladoDoQuadrado = float(input("Digite o valor referente ao tamanho do lado do quadrado: "))

#Imprime uma linha em branco para dar espaço entre a entrada do usuário e os resultados
print(" ")

#Calcula a área do quadrado
areaDoQuadrado = ladoDoQuadrado ** 2

#Calcula o perímetro do quadrado
perimetroDoQuadrado = ladoDoQuadrado * 4

#Imprime a área do quadrado com uma mensagem para o usuário
print("A área do seu quadrado é: ", areaDoQuadrado)

#Imprime o perímetro do quadrado com uma mensagem para o usuário
print("O perimetro do seu quadrado é: ", perimetroDoQuadrado)