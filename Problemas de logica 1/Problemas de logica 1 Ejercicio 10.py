# Solicitar número con validación
while True:
    try:
        numero = float(input("Ingrese un número real (positivo o negativo): "))
        break
    except ValueError:
        print("Error: Debe ingresar un número válido (ej: 15, -3.14, 7.5)")

# Calcular valor absoluto
absoluto = abs(numero)

# Mostrar resultado formateado
print(f"\nValor original: {numero:.2f}")
print(f"Valor absoluto: {absoluto:.2f}")