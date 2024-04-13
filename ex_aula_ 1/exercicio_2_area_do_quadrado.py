##Exercício 3:
##Faça um programa que calcule e mostre o IMC (índice de massa corporal) de uma pessoa, considerando que ela irá dizer qual o seu peso 
#e qual a sua altura (imc = peso/(altura*altura)).

#Solicita ao usuário que insira sua altura em metros e armazena o valor como uma variável de ponto flutuante
alturaUsuário = float(input("Digite a sua altura em metros: "))

#Imprime uma linha em branco para dar espaço entre a entrada do usuário e a próxima solicitação
print(" ")

#Solicita ao usuário que insira seu peso em quilogramas e armazena o valor como uma variável em ponto flutuante
pesoUsuário = float(input("Digite seu peso em KG: "))

#Imprime uma linha em branco para dar espaço entre a entrada do usuário e os resultados
print(" ")

#Calcula o Indice de Massa Corporal (IMC) usando a fórmula de peso/(altura * altura)
imc = pesoUsuário/(alturaUsuário * alturaUsuário)

#Imprime o resultado do cálculo do IMC com uma mensagem para o usuário
print("Seu IMC é:", imc)

#Imprime uma linha em branco para dar espaço entre o resultado e a mensagem que será enviada a seguir
print(" ")

#Verifica em que faixa o IMC calculado se encontra e imprime uma mensagem apropriada
if imc < 16.9:
#Se o IMC for menor que 16.9, imprime uma mensagem indicando que o usuário está muito abaixo do peso
  print("Você está muito abaixo do peso, por favor consulte um nutricionista!")
elif 16.9 <= imc <= 18.4:
#Se o IMC estiver entre 16.9 e 18.4, imprime uma mensagem para o usuário indicando que ele está abaixo do peso
  print("Você está abaixo do peso, por favor consulte um nutricionista!")
elif 18.5 <= imc <= 24.9:
#Se o IMC estiver entre 18.5 e 24.9, imprime uma mensagem indicando que o peso do usuário está normal
  print("Seu peso está normal, mas não deixe de fazer um acompanhamento com um nutricionista.")
elif 25 <= imc <=29.9:
#Se o IMC estiver entre 25 e 29.9, imprime uma mensagem indicando que o usuário está muito acima do peso
  print("Você está muito acima do peso, por favor consulte um nutricionista!")
elif 30 <= imc <= 34.9:
#Se o IMC estiver entre 30 e 34.9, imprime uma mensagem indicando que o usuário apresenta Obesidade Grau I
  print("Você apresenta Obesidade Grau I, por favor consulte um nutricionista!")
elif 35 <= imc <= 40:
#Se o IMC estiver entre 35 e 40, imprime uma mensagemm indicando que o usuário apresenta Obesidade Grau II
  print("Você apresenta Obesidade Grau II, por favor consulte um nutricionista!")
else:
#Se todas as alternativas anteriores não forem verdadeiras e o IMC for maior que 40, imprime uma mensagem indicando que o usuário apresenta Obesidade Grau III
  print("Você apresenta Obesidade Grau III, por favor consulte um nutricionista!")  