Archivo sugerido: ejercicio3_suma_digitos.py

def suma_digitos_potencia(base, exponente):
    potencia = base ** exponente
    suma = sum(int(digito) for digito in str(potencia))
    return suma

# Prueba
if __name__ == "_main_":
    base = int(input("Ingrese la base: "))
    exponente = int(input("Ingrese el exponente: "))
    resultado = suma_digitos_potencia(base, exponente)
    print(f"La suma de los dígitos de {base}^{exponente} es: {resultado}")
