# Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar.
# Você deve poder calcular a soma (+), subritração(-), multiplicação (*) e divisão(/).
# Exiba o resultado da operação solicitada.

#solicitar o primeiro número ao usuário

from winreg import EnableReflectionKey


primeiro = int(input("Vamos calcular! Digite o primeiro número: "))

#solicitar o segundo número ao usuário
segundo = int(input("Digite o segundo número: "))

#solicitar a operação ao usuário
operacao = int(input("Ok! Agora digite a operação você deseja fazer com o seu número:\n 1 para soma (+)\n 2 para subtração (-)\n 3 para multiplicação (*)\n 4 para divisão (/)"))



#apresentar o resultado

if operacao == 1:
    print (primeiro+segundo)

elife: operacao == 2
    print (primeiro-segundo)

elife: operacao == 3
    print (primeiro*segundo)
    





