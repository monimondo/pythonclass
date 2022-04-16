# Exercício 4.9_Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
# O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar.
# O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

#solicitar os dados ao usuário
valor_casa = float(input("Qual o valor do imóvel que você deseja financiar?"))
salario = float(input("Qual sua renda mensal?"))
prazo = int(input("Em quantos anos você quer financiar seu novo imóvel?"))


#converter o numedo de anos em meses
prazo = prazo * 12

#verificar o valor da prestação
prestacao = valor_casa/prazo

#verificar percentual em relação ao salário
percentual = salario * (30/100)

#informar o resultado ao usuário
if prestacao <= percentual:
    print(f"Parabéns, o valor da prestação será de R$: {prestacao:6.2f}, seu empréstimo pode ser aprovado.")

else:
    print(f"O valor da prestação é de R$: {prestacao:6.2f}, isso representa mais de 30% do que você ganha. O emprestimo foi negado.")
