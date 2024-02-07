def calcula_imc(altura, peso):
    imc = peso / (altura * altura)
    if imc < 18.5:
        print(f"com imc de {imc:} você esta abaixo de peso")
    elif 24.9 >= imc >= 18.5:
        print(f"com IMC de {imc} você esta com o peso normal")
    elif 29.9 >= imc >= 25:
        print(f"com IMC de {imc} você esta acima do peso ")
    elif 34.9 >= imc >= 30.0:
        print(f"com IMC de {imc} você esta com obesidade grau 1")
    elif 39.9 >= imc >= 35:
        print(f"com IMC de {imc} você esta com obesidade grau 2")
    else:
        print(f"com IMC de {imc} você esta com Obesidade grau 3(Obesidade Mórbida)")


calcula_imc(1.80, 71)
