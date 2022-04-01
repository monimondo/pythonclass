#Exercício 3.12 - Escreva um programa que calcule o tempo de uma viagem de carro.
#Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

#perguntar ao usuário a distância a percorrer
distancia = float(input("Quantos km tem até o seu destino?: "))

#perguntar ao usuário a velocidade média que ele vai rodar
velocidade_media = float(input("Em que velocidade média você pretende dirigir? "))

# calcular o tempo necessário para a viagem
tempo_viagem = distancia / velocidade_media

#apresentar o resultado
if tempo_viagem < 1:
    tempo_minutos = tempo_viagem * 60
    print(f"O tempo de viagem será: {tempo_minutos:.0f} min")
else:
    print(f"O tempo de viagem será: {tempo_viagem:.2f} h")