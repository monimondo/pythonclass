from io import RawIOBase
from tkinter import RADIOBUTTON

#Construa um programa no qual um usuário informe a sua 
#estatura em metros e o programa converta-a para centímetros.

# Solicitar a idade do usuário em metros
altura= float(input('Qual a sua altura em metros?: '))

# Converter a idade do usuário de metros para centímetros
centimetros = altura * 100

# Apresentar a idade do usuário em centímetros

print(f"Esse valor em centímetros é: {centimetros} cm")
