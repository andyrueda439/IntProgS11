def factorial(n):
    if n < 0:
        return "El número debe ser un entero no negativo."
    elif n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

# Ejemplo de uso
numero = int(input("Introduce un número entero no negativo: "))
print(f"El factorial de {numero} es: {factorial(numero)}")
