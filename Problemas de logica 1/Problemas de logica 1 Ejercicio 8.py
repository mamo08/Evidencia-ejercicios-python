# Validar entrada del precio
while True:
    try:
        precio = float(input("Ingrese el valor del producto: "))
        if precio >= 0:
            break
        else:
            print("Error: El valor no puede ser negativo")
    except ValueError:
        print("Error: Debe ingresar un valor numérico válido")

# Calcular descuento del 10%
precio_final = precio * 0.90

# Mostrar resultado formateado
print(f"\nValor original: ${precio:,.2f}")
print(f"Precio con 10% de descuento: ${precio_final:,.2f}")