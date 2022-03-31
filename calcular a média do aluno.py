# from tkinter import dialog
# Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado. 
# Para ser aprovado a média do aluno deve ser maior ou igual a 7.


# Listar as notas
nota1= int(input('Primeira nota: '))
nota2= int(input('Segunda nota: '))
nota3= int(input('Terceira nota: '))

# Fazer a média
media = (nota1 + nota2 + nota3) / 3

# Estabelecer a média para aprovado ou reprovado

print ("A média do aluno é:" + str(media)) 

# Apresentar o resultado com mensagem motivacional.
if media > 7 : print ('Parabéns! o aluno está aprovado.')
if media < 7 : print ('Lamentamos, o aluno está reprovado.')