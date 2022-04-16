# **Interpolação de String (str)**
# substituir as posições fixas e demarcadas na string por valores de variáveis.
# Usa-se o f ou F de format antes das aspas e coloque entre chaves o valor a ser chamado.

# Exercício 3.4 - Escreva uma expressão para determinar se uma pessoa deve ou não pagar imposto.
# Considerando que paga imposto pessoas que recebem mais que R$ 1.900,00.

#perguntar o salário
print ("Vamos descobrir se você precisa pagar imposto?")
salario = int (input ("Qual o seu salário?" ))
imposto = True

 
 #determinar se paga ou não imposto
if salario > 1900 and < 2800:
    valor1 = salario (7/100)
    print (F"Você pagara imposto? {imposto} e ele será de R$ {valor1}")

elif salario > 2800 and < 3700:
    valor2 = salario * (15/100)
    print (f"Você pagará imposto? {imposto} e ele será de R$ {valor2}")

elif salario > 3700 and salario < 4600:
    valor3 = salario * (22.5/100)
    print(f"você pagara imposto? {imposto} e ele será de R$ {valor3}") 
    
elif salario > 3700 and salario < 4600:
    valor4 = salario * (27.5/100)
    print(f"você pagara imposto? {imposto} e ele será de R$ {valor4}")
    
else: 
    print(f"você pagara imposto? {not imposto}")