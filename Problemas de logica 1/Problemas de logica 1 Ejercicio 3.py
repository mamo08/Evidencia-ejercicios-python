# Solicitar precio del electrodoméstico con validación
while True:
    try:
        precio = float(input("Ingrese el precio del electrodoméstico: "))
        if precio > 0:
            break
        else:
            print("Error: El precio debe ser un valor positivo")
    except ValueError:
        print("Error: Debe ingresar un número válido")

# Solicitar plazo en meses con validación
while True:
    try:
        meses = int(input("Ingrese el plazo en meses: "))
        if meses > 0:
            break
        else:
            print("Error: El plazo debe ser un entero positivo")
    except ValueError:
        print("Error: Debe ingresar un número entero válido")

# Calcular valor total con incremento del 5% por mes
total = precio * (1 + 0.05 * meses)

# Calcular valor de la cuota mensual
cuota_mensual = total / meses

# Mostrar resultado
print(f"\nEl valor fijo de cada cuota mensual será: ${cuota_mensual:,.2f}")