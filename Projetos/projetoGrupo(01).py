import time

# Introdução ao Programa
print("=======Bem vindo ao calculador de IMC=======")
# Utilização do Time.sleep para dar uma dinamica de tempo ao programa
time.sleep(2)

# Pedido ao Utilizador da sua Altura
userAltura = float(input("Digite a sua Altura: "))

time.sleep(2)

# Pedido ao utilizador do seu Peso
userPeso = int(input("Digite o seu Peso: "))

# Imitação de um Calculo
print("Calculando...")
time.sleep(0.5)
print("..")
time.sleep(0.5)
print("...")
time.sleep(0.5)
print("..")
time.sleep(2)

# Formula de Calculo do IMC utilizando os dados introduzidos pelo utilizador
imcCalculo = userPeso / (userAltura * userAltura)

print("==================================================================================")

# Comparações para ver qual o resultado de IMC do Utilizador
if imcCalculo < 18.5:
    print(f"o seu IMC é {imcCalculo:.1f}, encontra-se abaixo de peso")

elif 18.5 <= imcCalculo < 24.9:
    print(f"o seu IMC é {imcCalculo:.1f}, encontra-se no peso normal")

elif 25.0 <= imcCalculo < 29.9:
    print(f"o seu IMC é {imcCalculo:.1f}, encontra-se em Sobrepeso")

elif 30.0 <= imcCalculo < 34.9:
    print(f"o seu IMC é {imcCalculo:.1f}, encontra-se em Obesidade Grau 1")

elif 35.0 <= imcCalculo < 39.9:
    print(f"o seu IMC é {imcCalculo:.1f}, encontra-se em Obesidade Grau 2")

elif imcCalculo >= 40.0:
    print(f"o seu IMC é {imcCalculo:.1f}, encontra-se em Obesidade Grau 3(Obesidade Mórbida)")

print("==================================================================================")
k
