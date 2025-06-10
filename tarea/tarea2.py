def decimal_a_binario(n):
    if n == 0:
        return "0"
    binario = ""
    while n > 0:
        binario = str(n % 2) + binario
        n //= 2
    return binario

if __name__ == "_main_":
    numero = int(input("Ingrese un número entero positivo: "))
    print(f"La representación binaria de {numero} es: {decimal_a_binario(numero)}")