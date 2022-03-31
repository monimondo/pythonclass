#Exercício 3.11 - Faça um programa que solicite o preço de uma mercadoria
# e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.

#solicitar ao usuário o preço da mercadoria
preco_mercadoria = float(input("Qual o valor do seu produto? "))
#solicitar ao usuário o valor do desconto em percentuais
percentual_desconto = float (input ("Qual desconto você quer aplciar sobre o valor do seu produto?" ))
# calcular o desconto 
desconto = preco_mercadoria * percentual_desconto / 100
valor_total = preco_mercadoria - desconto
# apresentar o valor do desconto e o novo valor da mercadoria 
print (f"O desconto aplicado foi de: R${desconto:.2f}")
print (f"O valor final do produto é de R${valor_total:.2f}")