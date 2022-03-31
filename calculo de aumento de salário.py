#Exercício 3.10 - Faça um programa que calcule o aumento de um salário.

#perguntar ao usuário qual o salário Dele
salario = float (input ("Qual o valor do seu salário atual? "))

#perguntar ao uusário qual o percentual de aumento ele está somando
porcentagem_aumento = float (input ("Quantos por cento você deseja receber de aumento? "))

#calcular o salario somado ao aumento
porcentagem = porcentagem_aumento / 100
aumento = salario * porcentagem

#resultado do calculo
novo_salario = salario + aumento

#apresentar o resultado
print (f"O valor do aumento será de: R${aumento:.2f}")
print (f"O salário ajustado será de R$ {novo_salario:.2f}")
