# faça um programa que leia um numero inteiro qualquer e mostre a sua tabuada.

x = 0
tabuada = int(input("Qual tabuada você deseja ver?"))
while x <= 10:
    print(tabuada, "x", x, "=" , tabuada*x)
    x = x + 1

