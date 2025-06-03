#Calcular el area de un circulo
""" formula area = pi * (r * r)"""

import math

def calcular_area(radio):
    return math.pi * radio ** 2
    

def main():
    radio = float(input("Dame un numero: "))
    area = calcular_area(radio)
    print(f"El area del circulo es de: {area}")

main()