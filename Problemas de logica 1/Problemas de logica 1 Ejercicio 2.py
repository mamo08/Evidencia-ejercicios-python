# Leer primer número con validación
while True:
    try:
        num1 = float(input("Ingrese el primer número: "))
        break
    except ValueError:
        print("Error: Debe ingresar un número válido")

# Leer segundo número con validación
while True:
    try:
        num2 = float(input("Ingrese el segundo número: "))
        break
    except ValueError:
        print("Error: Debe ingresar un número válido")

# Calcular suma resta y producto
suma = num1 + num2
resta = num1 - num2
producto = num1 * num2

# Mostrar división y módulo con validación de cero
if num2 != 0:
    cociente = num1 / num2
    modulo = num1 % num2
else:
    cociente = "Error: división por cero"
    modulo = "Error: módulo por cero"

# Mostrar resultados 
print("\nResultados:")
print(f"Producto: {producto}")
print(f"Módulo: {modulo}")
print(f"Cociente: {cociente}")
print(f"Suma: {suma}")
print(f"Resta: {resta}")