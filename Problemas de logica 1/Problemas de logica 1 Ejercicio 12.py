# Validación de entrada para temperatura Celsius
while True:
    try:
        celsius = float(input("Ingrese la temperatura en grados Celsius: "))
        break
    except ValueError:
        print("Error: Debe ingresar un valor numérico válido (ej: 25, -3.5, 10.75)")

# Fórmula de conversión: Fahrenheit = (Celsius × 9/5) + 32
fahrenheit = (celsius * 9/5) + 32

# Mostrar resultado formateado
print(f"\n{celsius}°C equivale a {fahrenheit:.2f}°F")