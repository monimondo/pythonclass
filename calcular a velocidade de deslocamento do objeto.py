#Construa um programa que receba do usuário a variação do 
#deslocamento de um objeto (em metros) e a variação do tempo percorrido (em segundo). Ao fim, o programa deve calcular a 
#velocidade média, em m/s, do objeto

# Solicitar o deslocamento do objeto
deslocamento= float(input('Qual o deslocamento do objeto?: '))
tempo= int(input('Quanto tempo demorou para ocorrer o deslocamento?: '))

# Converter a idade do usuário de metros para centímetros
resultado = deslocamento / tempo

# Apresentar a idade do usuário em centímetros

print(f"A velocidade do objeto foi de: {resultado:.1f} m/s")