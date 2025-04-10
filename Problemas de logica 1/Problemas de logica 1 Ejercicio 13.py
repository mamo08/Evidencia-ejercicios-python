# Inicializar el factorial en 1
factorial = 1

# Calcular el factorial multiplicando desde 1 hasta 5
for numero in range(1, 6):
    factorial *= numero  # Equivalente a: factorial = factorial * numero

# Mostrar el resultado
print(f"El factorial de 5 es: {factorial}")