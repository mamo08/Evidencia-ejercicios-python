# Validar cantidad base
while True:
    try:
        cantidad = float(input("Ingrese la cantidad base: "))
        if cantidad >= 0:
            break
        else:
            print("Error: La cantidad no puede ser negativa")
    except ValueError:
        print("Error: Debe ingresar un número válido")

# Validar porcentaje
while True:
    try:
        porcentaje = float(input("Ingrese el porcentaje a calcular (ej: 15, 25.5, -10): "))
        break
    except ValueError:
        print("Error: Debe ingresar un número válido")

# Calcular el porcentaje
resultado = cantidad * (porcentaje / 100)

# Mostrar resultado formateado
print(f"\n{porcentaje}% de {cantidad:,.2f} = {resultado:+,.2f}")